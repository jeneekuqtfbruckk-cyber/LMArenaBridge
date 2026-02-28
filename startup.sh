#!/bin/bash
# LMArenaBridge HF Spaces 启动脚本
# 从环境变量注入 arena auth token 到 config.json

echo "🚀 LMArenaBridge Startup Script"

# 如果 config.json 不存在，创建默认配置
if [ ! -f config.json ]; then
    echo '{"password":"admin","auth_token":"","auth_tokens":[],"cf_clearance":"","api_keys":[],"prune_invalid_tokens":false,"persist_arena_auth_cookie":false}' > config.json
    echo "📝 Created default config.json"
fi

# 如果设置了 ARENA_AUTH 环境变量，注入到 config.json
if [ -n "$ARENA_AUTH" ]; then
    python3 -c "
import json, os
config_path = 'config.json'
try:
    with open(config_path) as f:
        config = json.load(f)
except:
    config = {}

token = os.environ.get('ARENA_AUTH', '')
if token:
    config.setdefault('auth_tokens', [])
    if token not in config['auth_tokens']:
        config['auth_tokens'].append(token)
    config['auth_token'] = token
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
    print(f'✅ Injected auth token into config.json (length: {len(token)} chars)')
else:
    print('⚠️  ARENA_AUTH env var is empty')
"
else
    echo "⚠️  No ARENA_AUTH env var set. You can add tokens via the dashboard at /dashboard"
fi

echo "🌐 Starting LMArenaBridge on port 7860..."

# 启动主程序
exec python3 src/main.py

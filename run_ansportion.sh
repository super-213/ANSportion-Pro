#!/bin/bash

# ANSportion 启动脚本
# 自动激活虚拟环境并运行程序

echo "========================================"
echo "  ANSportion 启动脚本"
echo "========================================"
echo ""

# 检查虚拟环境是否存在
if [ ! -d "venv" ]; then
    echo "❌ 虚拟环境不存在！"
    echo "请先运行安装脚本："
    echo "  bash install_mac.sh"
    exit 1
fi

# 检查是否需要 sudo
if [ "$1" == "sudo" ] || [ "$1" == "--sudo" ]; then
    echo "🔐 以管理员权限运行..."
    sudo venv/bin/python3 ANSportion.py
else
    echo "🚀 启动 ANSportion..."
    echo ""
    echo "💡 提示：如需管理员权限（WiFi、DOS攻击等），请使用："
    echo "   bash run_ansportion.sh sudo"
    echo ""
    source venv/bin/activate
    python3 ANSportion.py
    deactivate
fi

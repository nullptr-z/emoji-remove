#!/bin/bash
# 安装 remove-emoji CLI 工具

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_METHOD=""

echo "=== Remove Emoji CLI 安装脚本 ==="
echo ""
echo "请选择安装方式："
echo "1) 全局安装 (pip install -e .)"
echo "2) 创建 shell 别名"
echo "3) 仅显示使用说明"
echo ""
read -p "请输入选项 [1-3]: " choice

case $choice in
    1)
        echo ""
        echo "正在进行全局安装..."
        cd "$SCRIPT_DIR"
        pip3 install -e .
        echo ""
        echo "✅ 安装成功！现在可以在任何地方使用 'remove-emoji' 命令"
        echo ""
        echo "测试命令："
        echo "  remove-emoji --help"
        ;;

    2)
        echo ""
        echo "正在创建 shell 别名..."

        # 检测 shell 类型
        if [[ "$SHELL" == *"zsh"* ]]; then
            RC_FILE="$HOME/.zshrc"
        else
            RC_FILE="$HOME/.bashrc"
        fi

        ALIAS_LINE="alias remove-emoji='python \"$SCRIPT_DIR/remove_emoji.py\"'"

        # 检查是否已存在
        if grep -q "alias remove-emoji=" "$RC_FILE" 2>/dev/null; then
            echo "⚠️  别名已存在于 $RC_FILE"
            read -p "是否覆盖? [y/N]: " overwrite
            if [[ "$overwrite" =~ ^[Yy]$ ]]; then
                # 删除旧的，添加新的
                sed -i.bak '/alias remove-emoji=/d' "$RC_FILE"
                echo "$ALIAS_LINE" >> "$RC_FILE"
                echo "✅ 别名已更新"
            else
                echo "跳过"
            fi
        else
            echo "$ALIAS_LINE" >> "$RC_FILE"
            echo "✅ 别名已添加到 $RC_FILE"
        fi

        echo ""
        echo "请运行以下命令使别名生效："
        echo "  source $RC_FILE"
        echo ""
        echo "或者重新打开终端窗口"
        ;;

    3)
        echo ""
        echo "=== 使用说明 ==="
        echo ""
        echo "方式 1: 直接使用 Python 脚本"
        echo "  python $SCRIPT_DIR/remove_emoji.py <文件路径>"
        echo ""
        echo "方式 2: 全局安装"
        echo "  cd $SCRIPT_DIR"
        echo "  pip install -e ."
        echo "  remove-emoji <文件路径>"
        echo ""
        echo "方式 3: 创建别名"
        echo "  echo \"alias remove-emoji='python $SCRIPT_DIR/remove_emoji.py'\" >> ~/.zshrc"
        echo "  source ~/.zshrc"
        echo ""
        echo "查看完整文档："
        echo "  cat $SCRIPT_DIR/REMOVE_EMOJI_README.md"
        ;;

    *)
        echo "无效的选项"
        exit 1
        ;;
esac

echo ""
echo "完成！"


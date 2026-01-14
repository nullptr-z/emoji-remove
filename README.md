# Remove Emoji CLI 工具

一个简单易用的命令行工具，用于移除文档中的 emoji 字符。

## 🚀 快速开始

### 安装

```sh
cd emoji-remove
python3 -m pip install -e .
```

### 使用

```sh
# 查看帮助
remove-emoji --help

# 移除 emoji（生成新文件）
remove-emoji document.md

# 移除 emoji（直接修改原文件）
remove-emoji document.md -i

# 指定输出文件
remove-emoji document.md -o clean.md
```

## ✅ 已完成配置

已将以下内容添加到 `~/.zshrc`：

```sh
# Python bin 路径
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
```

## 🚀 让配置生效

### 方式 1：重新加载配置（推荐）

在终端中运行：

```sh
source ~/.zshrc
```

## 📝 文档

- **[快速开始指南](./QUICK_START.md)** - 安装和配置说明
- **[完整文档](./REMOVE_EMOJI_README.md)** - 详细使用文档
- **[总结文档](./emoji_cli_summary.md)** - 功能总结

## 📦 文件说明

```
emoji-remove/
├── README.md                   # 本文件
├── remove_emoji.py             # 核心脚本
├── setup.py                    # Python 安装配置
├── install.sh                  # 交互式安装脚本
├── Makefile.emoji              # Make 命令
├── REMOVE_EMOJI_README.md      # 完整使用文档
├── QUICK_START.md              # 快速开始指南
└── emoji_cli_summary.md        # 功能总结
```

## ✨ 特性

- 🎯 **精确删除**：只删除 emoji，不影响中文、英文、代码等内容
- 🔒 **安全操作**：默认不修改原文件
- 📝 **格式保持**：完整保留文档格式、缩进、空白符
- 🚀 **简单易用**：一行命令搞定
- 📦 **零依赖**：不需要安装任何第三方包

## 🔧 三种使用方式

### 方式 1：全局命令（推荐）

```sh
# 安装
cd emoji-remove
python3 -m pip install -e .

# 添加到 PATH
echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# 使用
remove-emoji file.md -i
```

### 方式 2：别名（最简单）

```sh
# 添加别名
echo "alias remove-emoji='python $(pwd)/remove_emoji.py'" >> ~/.zshrc
source ~/.zshrc

# 使用
remove-emoji file.md -i
```

### 方式 3：直接调用

```sh
python emoji-remove/remove_emoji.py file.md -i
```

## 📖 使用示例

```sh
# 处理单个文件
remove-emoji space/api-doc.md -i

# 批量处理
for file in space/*.md; do
    remove-emoji "$file" -i
done

# 生成新文件保留原文件
remove-emoji document.md -o document-clean.md
```

## 🛠️ 开发

```sh
# 安装（开发模式）
python3 -m pip install -e .

# 测试
make -f Makefile.emoji test

# 卸载
python3 -m pip uninstall remove-emoji
```

## 📄 License

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

更多详细信息请查看 [完整文档](./REMOVE_EMOJI_README.md)
# emjio-remove

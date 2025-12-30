#!/usr/bin/env python3
"""
ANSportion Mac 兼容性测试脚本
用于检查系统环境和依赖库是否正确安装
"""

import sys
import platform
import importlib.util

def check_python_version():
    """检查 Python 版本"""
    print("=" * 60)
    print("1. 检查 Python 版本")
    print("=" * 60)
    version = sys.version_info
    print(f"Python 版本: {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 11:
        print("✅ Python 版本符合要求 (>= 3.11)")
        return True
    elif version.major == 3 and version.minor >= 8:
        print("⚠️  Python 版本可用但建议升级到 3.11+")
        return True
    else:
        print("❌ Python 版本过低，需要 3.8 或更高版本")
        return False

def check_system():
    """检查操作系统"""
    print("\n" + "=" * 60)
    print("2. 检查操作系统")
    print("=" * 60)
    system = platform.system()
    print(f"操作系统: {system}")
    print(f"系统版本: {platform.platform()}")
    
    if system == "Darwin":
        print("✅ 运行在 macOS 上")
        return True
    else:
        print(f"⚠️  当前系统是 {system}，此测试脚本专为 macOS 设计")
        return True

def check_library(lib_name, required=True):
    """检查单个库是否安装"""
    spec = importlib.util.find_spec(lib_name)
    if spec is not None:
        try:
            module = importlib.import_module(lib_name)
            version = getattr(module, '__version__', '未知版本')
            print(f"  ✅ {lib_name:15s} - 已安装 (版本: {version})")
            return True
        except Exception as e:
            print(f"  ⚠️  {lib_name:15s} - 已安装但导入失败: {e}")
            return False
    else:
        status = "❌ 必需" if required else "⚠️  可选"
        print(f"  {status} {lib_name:15s} - 未安装")
        return not required

def check_libraries():
    """检查所有依赖库"""
    print("\n" + "=" * 60)
    print("3. 检查依赖库")
    print("=" * 60)
    
    # 必需的库
    required_libs = [
        "requests",
        "validators",
        "urllib3",
        "tqdm",
        "psutil",
        "colorama",
        "cryptography",
    ]
    
    # 可选的库
    optional_libs = [
        "pywifi",      # Mac 上功能受限
        "PIL",         # Pillow
        "pyfiglet",
    ]
    
    print("\n必需的库:")
    required_ok = all(check_library(lib, required=True) for lib in required_libs)
    
    print("\n可选的库:")
    optional_ok = all(check_library(lib, required=False) for lib in optional_libs)
    
    # 检查 ipaddress（Python 3.3+ 内置）
    print("\n内置模块:")
    check_library("ipaddress", required=True)
    
    # Windows 专用库检查
    print("\nWindows 专用库（Mac 不需要）:")
    spec = importlib.util.find_spec("comtypes")
    if spec is None:
        print("  ✅ comtypes - 未安装（正确，Mac 不需要）")
    else:
        print("  ⚠️  comtypes - 已安装（Mac 不需要此库）")
    
    return required_ok

def check_network():
    """检查网络功能"""
    print("\n" + "=" * 60)
    print("4. 检查网络功能")
    print("=" * 60)
    
    try:
        import socket
        print("  ✅ socket 模块可用")
        
        # 测试基本网络连接
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            print("  ✅ 网络连接正常")
            return True
        except Exception as e:
            print(f"  ⚠️  网络连接测试失败: {e}")
            return False
    except Exception as e:
        print(f"  ❌ socket 模块错误: {e}")
        return False

def check_permissions():
    """检查权限"""
    print("\n" + "=" * 60)
    print("5. 检查权限")
    print("=" * 60)
    
    import os
    if os.geteuid() == 0:
        print("  ✅ 以 root 权限运行")
        print("  ℹ️  所有功能都可用")
    else:
        print("  ℹ️  以普通用户权限运行")
        print("  ⚠️  某些功能需要 root 权限：")
        print("     - WiFi 相关功能")
        print("     - 原始套接字（某些攻击功能）")
        print("  💡 使用 'sudo python3 ANSportion.py' 获取完整功能")
    
    return True

def test_basic_functionality():
    """测试基本功能"""
    print("\n" + "=" * 60)
    print("6. 测试基本功能")
    print("=" * 60)
    
    tests_passed = 0
    tests_total = 0
    
    # 测试 1: 导入主要模块
    tests_total += 1
    try:
        import socket
        import threading
        import random
        print("  ✅ 核心模块导入成功")
        tests_passed += 1
    except Exception as e:
        print(f"  ❌ 核心模块导入失败: {e}")
    
    # 测试 2: 网络功能
    tests_total += 1
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.close()
        print("  ✅ Socket 创建成功")
        tests_passed += 1
    except Exception as e:
        print(f"  ❌ Socket 创建失败: {e}")
    
    # 测试 3: 系统命令
    tests_total += 1
    try:
        import os
        result = os.system("echo 'test' > /dev/null 2>&1")
        if result == 0:
            print("  ✅ 系统命令执行成功")
            tests_passed += 1
        else:
            print("  ⚠️  系统命令执行异常")
    except Exception as e:
        print(f"  ❌ 系统命令执行失败: {e}")
    
    print(f"\n测试结果: {tests_passed}/{tests_total} 通过")
    return tests_passed == tests_total

def print_summary(results):
    """打印总结"""
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)
    
    all_passed = all(results.values())
    
    for test_name, passed in results.items():
        status = "✅" if passed else "❌"
        print(f"{status} {test_name}")
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 所有测试通过！ANSportion 可以在 Mac 上运行")
        print("\n运行方式:")
        print("  python3 ANSportion.py")
        print("\n如需完整功能（WiFi、原始套接字等）:")
        print("  sudo python3 ANSportion.py")
    else:
        print("⚠️  部分测试未通过，请检查上述问题")
        print("\n建议:")
        print("  1. 运行安装脚本: bash install_mac.sh")
        print("  2. 或手动安装依赖: pip3 install -r requirements_mac.txt")
    print("=" * 60)

def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("  ANSportion Mac 兼容性测试")
    print("=" * 60)
    print()
    
    results = {
        "Python 版本": check_python_version(),
        "操作系统": check_system(),
        "依赖库": check_libraries(),
        "网络功能": check_network(),
        "权限检查": check_permissions(),
        "基本功能": test_basic_functionality(),
    }
    
    print_summary(results)
    
    return 0 if all(results.values()) else 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  测试被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ 测试过程中发生错误: {e}")
        sys.exit(1)

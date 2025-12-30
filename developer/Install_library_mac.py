import os
import sys

def install_library_main():
    print("=" * 60)
    print("  ANSportion Mac 依赖库安装工具")
    print("=" * 60)
    print("\n注意：comtypes 是 Windows 专用库，Mac 不需要安装\n")
    
    choose = input("1. 选择性安装第三方库\n2. 一键安装第三方库\n3. 查看所有库是否装好\n:")
    
    if choose == "1":
        print("开始安装依赖第三方库")
        try:
            pywifi = input("是否下载 pywifi 库? (Mac 上功能受限) (y/n):")
            if pywifi in ["y","Y"]:
                os.system("pip3 install pywifi")
            else:
                print("已取消下载")
            
            requests = input("是否下载 requests 库? (y/n):")
            if requests in ["y","Y"]:
                os.system("pip3 install requests")
            else:
                print("已取消下载")
            
            validators = input("是否下载 validators 库? (y/n):")
            if validators in ["y","Y"]:
                os.system("pip3 install validators")
            else:
                print("已取消下载")
            
            urllib3 = input("是否下载 urllib3 库? (y/n):")
            if urllib3 in ["y","Y"]:
                os.system("pip3 install urllib3")
            else:
                print("已取消下载")
            
            tqdm = input("是否下载 tqdm 库? (y/n):")
            if tqdm in ["y","Y"]:
                os.system("pip3 install tqdm")
            else:
                print("已取消下载")
            
            psutil = input("是否下载 psutil 库? (y/n):")
            if psutil in ["y","Y"]:
                os.system("pip3 install psutil")
            else:
                print("已取消下载")
            
            ipaddress = input("是否下载 ipaddress 库? (y/n):")
            if ipaddress in ["y","Y"]:
                os.system("pip3 install ipaddress")
            else:
                print("已取消下载")
            
            colorama = input("是否下载 colorama 库? (y/n):")
            if colorama in ["y","Y"]:
                os.system("pip3 install colorama")
            else:
                print("已取消下载")
            
            pyinstaller = input("是否下载 pyinstaller 库? (y/n):")
            if pyinstaller in ["y","Y"]:
                os.system("pip3 install pyinstaller")
            else:
                print("已取消下载")
            
            cryptography = input("是否下载 cryptography 库? (y/n):")
            if cryptography in ["y","Y"]:
                os.system("pip3 install cryptography")
            else:
                print("已取消下载")
            
            Pillow = input("是否下载 Pillow 库? (y/n):")
            if Pillow in ["y","Y"]:
                os.system("pip3 install Pillow")
            else:
                print("已取消下载")
            
            pyfiglet = input("是否下载 pyfiglet 库? (y/n):")
            if pyfiglet in ["y","Y"]:
                os.system("pip3 install pyfiglet")
            else:
                print("已取消下载")
            
            print("\n⚠️  注意：comtypes 是 Windows 专用库，Mac 不需要安装")
            
        except Exception as e:
            print(f"安装失败: {e}")
        print("安装完成")
    
    elif choose == "2":
        print("开始一键安装第三方库（Mac 版本）")
        print("⚠️  注意：comtypes 已排除（Windows 专用）")
        try:
            # Mac 版本：排除 comtypes
            os.system("pip3 install pywifi requests validators urllib3 tqdm psutil ipaddress colorama pyinstaller cryptography Pillow pyfiglet")
        except Exception as e:
            print(f"安装失败: {e}")
        print("安装完成")
    
    elif choose == "3":
        print("开始检查所有库是否装好")
        try:
            libraries = [
                "pywifi",
                "requests",
                "validators",
                "urllib3",
                "tqdm",
                "psutil",
                "ipaddress",
                "colorama",
                "pyinstaller",
                "cryptography",
                "Pillow",
                "pyfiglet"
            ]
            
            for lib in libraries:
                print(f"\n开始检查 {lib} 库")
                print(f"{'='*80}")
                result = os.system(f"pip3 show {lib}")
                if result == 0:
                    print(f"{lib} 库已装好")
                else:
                    print(f"⚠️  {lib} 库未安装")
                print(f"{'='*80}")
            
            print("\n⚠️  注意：comtypes 是 Windows 专用库，Mac 不需要检查")
            print("检查完成")
            
        except Exception as e:
            print(f"检查失败:\n{e}")

if __name__ == "__main__":
    if sys.platform != "darwin":
        print("⚠️  警告：此脚本专为 macOS 设计")
        print(f"当前系统：{sys.platform}")
        confirm = input("是否继续？(y/n): ")
        if confirm.lower() not in ['y', 'yes']:
            sys.exit(0)
    
    install_library_main()

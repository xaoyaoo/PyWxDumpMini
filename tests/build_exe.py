# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         gen_exe.py
# Description:  
# Author:       xaoyaoo
# Date:         2023/11/10
# -------------------------------------------------------------------------------
import shutil
import site
import os

code = """
from pywxdump_mini import read_info
a = read_info(is_logging=True)
with open("wx_info.txt", "w", encoding="utf-8") as f:
    f.write(str(a))
"""

spec_content = '''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['tmp.py'],
             pathex=[],
             binaries=[],
             hiddenimports={hidden_imports},
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='wxdump',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,  # 启用压缩
          console=True,  # 使用控制台 
          disable_windowed_traceback=True,  # 不禁用堆栈跟踪
          argv_emulation=False, # 不模拟命令行参数
          target_arch=None,  # 自动检测目标 CPU 架构
          codesign_identity=None,  # 不签名应用程序
          entitlements_file=None,  # 不使用 entitlements 文件
          onefile=True,  # 生成单个可执行文件
          icon="icon.ico"
          )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='wxdump')

'''
# 创建文件夹
os.makedirs("dist", exist_ok=True)
# 当前文件所在目录
current_path = os.path.dirname(os.path.abspath(__file__))
shutil.copy(os.path.join(os.path.dirname(current_path), "pywxdump_mini", "simplify_wx_info.py"), "dist/tmp.py")  # 复制代码
shutil.copy(os.path.join(current_path, "icon.ico"), "dist/icon.ico")  # 复制图标

require_path = os.path.join(os.path.dirname(current_path), "requirements.txt")  # requirements.txt 路径
with open(require_path, "r", encoding="utf-8") as f:
    hidden_imports = f.read().splitlines()
hidden_imports = [i for i in hidden_imports if i not in ["setuptools", "wheel"]]  # 去掉setuptools、wheel

# 生成 spec 文件
spec_content = spec_content.format(hidden_imports=hidden_imports)
spec_file = os.path.join("dist", "pywxdump.spec")
with open(spec_file, 'w', encoding="utf-8") as f:
    f.write(spec_content.strip())

# 执行打包命令
cmd = f'pyinstaller --clean  --distpath=dist {spec_file}'
print(cmd)
# os.system(cmd)

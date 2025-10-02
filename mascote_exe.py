#!/usr/bin/env python3
"""
Script para compilar o MascoteApp em um executável Windows (.exe)

Este script automatiza o processo de criação de um executável usando PyInstaller.
Inclui todas as dependências necessárias e arquivos de recursos (ícones, GIFs).

Autor: Christian Vladimir Uhdre Mulato
Data: Campo Largo, 02 de Outubro de 2025.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

class MascoteCompiler:
    def __init__(self):
        self.script_dir = Path(__file__).parent.absolute()
        self.source_file = self.script_dir / "mascote.py"
        self.dist_dir = self.script_dir / "dist"
        self.build_dir = self.script_dir / "build"
        self.spec_file = self.script_dir / "mascote.spec"
        
        # Arquivos de recursos necessários
        self.resource_files = [
            "mascote.gif",
            "mascote.ico",
            "boneco.ico"
        ]
        
    def check_requirements(self):
        """Verifica se todos os requisitos estão instalados"""
        print("🔍 Verificando requisitos...")
        
        # Verifica se o arquivo principal existe
        if not self.source_file.exists():
            print(f"❌ Erro: {self.source_file} não encontrado!")
            return False
            
        # Verifica arquivos de recursos
        missing_resources = []
        for resource in self.resource_files:
            resource_path = self.script_dir / resource
            if not resource_path.exists():
                missing_resources.append(resource)
                
        if missing_resources:
            print(f"⚠️  Arquivos de recursos não encontrados: {', '.join(missing_resources)}")
            print("   O executável será criado, mas pode não funcionar corretamente.")
            
        return True
        
    def install_pyinstaller(self):
        """Instala o PyInstaller se não estiver disponível"""
        print("📦 Verificando PyInstaller...")
        
        try:
            import PyInstaller
            print("✅ PyInstaller já está instalado")
            return True
        except ImportError:
            print("📥 Instalando PyInstaller...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], 
                             check=True, capture_output=True, text=True)
                print("✅ PyInstaller instalado com sucesso")
                return True
            except subprocess.CalledProcessError as e:
                print(f"❌ Erro ao instalar PyInstaller: {e}")
                return False
                
    def clean_previous_builds(self):
        """Remove builds anteriores"""
        print("🧹 Limpando builds anteriores...")
        
        # Remove diretórios de build
        for directory in [self.dist_dir, self.build_dir]:
            if directory.exists():
                shutil.rmtree(directory)
                print(f"   Removido: {directory}")
                
        # Remove arquivo .spec se existir
        if self.spec_file.exists():
            self.spec_file.unlink()
            print(f"   Removido: {self.spec_file}")
            
    def create_executable(self):
        """Cria o executável usando PyInstaller"""
        print("🔨 Compilando executável...")
        
        # Monta comando do PyInstaller
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",                    # Arquivo único
            "--windowed",                   # Sem console
            "--name", "mascote",            # Nome do executável
            "--icon", "mascote.ico",        # Ícone do executável
            "--distpath", str(self.dist_dir),  # Diretório de saída
            "--workpath", str(self.build_dir), # Diretório de trabalho
            "--clean",                      # Limpa cache
            "--noconfirm",                  # Não pede confirmação
        ]
        
        # Adiciona arquivos de dados (recursos)
        for resource in self.resource_files:
            resource_path = self.script_dir / resource
            if resource_path.exists():
                cmd.extend(["--add-data", f"{resource_path};."])
                
        # Adiciona arquivo principal
        cmd.append(str(self.source_file))
        
        try:
            print(f"   Executando: {' '.join(cmd)}")
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print("✅ Compilação concluída com sucesso!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro durante a compilação:")
            print(f"   Código de saída: {e.returncode}")
            print(f"   Stdout: {e.stdout}")
            print(f"   Stderr: {e.stderr}")
            return False
            
    def copy_resources_to_dist(self):
        """Copia recursos necessários para o diretório dist"""
        print("📋 Copiando recursos adicionais...")
        
        if not self.dist_dir.exists():
            print("❌ Diretório dist não encontrado!")
            return False
            
        # Copia arquivos de recursos para junto do executável
        for resource in self.resource_files:
            resource_path = self.script_dir / resource
            if resource_path.exists():
                dest_path = self.dist_dir / resource
                shutil.copy2(resource_path, dest_path)
                print(f"   Copiado: {resource} → dist/")
                
        return True
        
    def verify_executable(self):
        """Verifica se o executável foi criado corretamente"""
        print("✅ Verificando executável...")
        
        exe_path = self.dist_dir / "mascote.exe"
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024 * 1024)
            print(f"✅ Executável criado: {exe_path}")
            print(f"   Tamanho: {size_mb:.2f} MB")
            
            # Lista todos os arquivos no diretório dist
            print("📁 Conteúdo do diretório dist:")
            for item in self.dist_dir.iterdir():
                if item.is_file():
                    item_size = item.stat().st_size / 1024
                    print(f"   📄 {item.name} ({item_size:.1f} KB)")
                    
            return True
        else:
            print("❌ Executável não foi criado!")
            return False
            
    def run_compilation(self):
        """Executa todo o processo de compilação"""
        print("🚀 Iniciando compilação do MascoteApp para Windows")
        print("=" * 60)
        
        # Verifica requisitos
        if not self.check_requirements():
            return False
            
        # Instala PyInstaller
        if not self.install_pyinstaller():
            return False
            
        # Limpa builds anteriores
        self.clean_previous_builds()
        
        # Cria executável
        if not self.create_executable():
            return False
            
        # Copia recursos
        if not self.copy_resources_to_dist():
            return False
            
        # Verifica resultado
        if not self.verify_executable():
            return False
            
        print("=" * 60)
        print("🎉 COMPILAÇÃO CONCLUÍDA COM SUCESSO!")
        print(f"📁 Executável disponível em: {self.dist_dir / 'mascote.exe'}")
        print()
        print("💡 Para distribuir o aplicativo:")
        print(f"   1. Copie todo o conteúdo da pasta: {self.dist_dir}")
        print("   2. Execute o arquivo mascote.exe")
        print()
        print("⚠️  Certifique-se de que os arquivos de recursos estão junto do .exe")
        
        return True

def main():
    """Função principal"""
    try:
        compiler = MascoteCompiler()
        success = compiler.run_compilation()
        
        if success:
            print("\n✅ Processo concluído com sucesso!")
            
            # Pergunta se quer testar o executável
            test_exe = input("\n🧪 Deseja testar o executável agora? (s/n): ").lower().strip()
            if test_exe in ['s', 'sim', 'y', 'yes']:
                exe_path = compiler.dist_dir / "mascote.exe"
                if exe_path.exists():
                    print("🚀 Executando teste do executável...")
                    subprocess.Popen([str(exe_path)], cwd=str(compiler.dist_dir))
                    print("   Executável iniciado em processo separado")
                    
        else:
            print("\n❌ Compilação falhou!")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Compilação cancelada pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
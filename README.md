# MascoteApp

Aplicativo para simular atividade no computador e manter o status ativo em aplicações como Microsoft Teams.

## Descrição

O MascoteApp é uma ferramenta que automatiza movimentos do mouse e pressiona teclas periodicamente para evitar que o sistema seja marcado como "ausente" em aplicativos de comunicação corporativa. O aplicativo possui interface gráfica intuitiva com mascote animado e sistema de logs detalhado.

## Funcionalidades

- Movimentação aleatória e natural do mouse com múltiplos algoritmos
- Simulação de pressionamento de teclas (barra de espaço)
- Tentativa de manter Microsoft Teams ativo
- Interface gráfica com mascote animado (GIF)
- Configuração de intervalos entre ações (padrão: 5 minutos)
- Sistema de logs detalhado em arquivo (cycle_log.txt)
- Som opcional a cada ciclo executado
- Tratamento robusto de erros
- Compilação para executável Windows

## Requisitos do Sistema

- Windows 7/8/10/11
- Python 3.7 ou superior
- Resolução mínima: 800x600 pixels

## Dependências

- Python 3.x (tkinter incluído)
- Pillow >= 10.0.0 (manipulação de imagens)
- pyautogui >= 0.9.54 (automação de interface)
- PyInstaller >= 6.0.0 (compilação para executável)

## Instalação e Execução

### Método 1: Executar com Python

1. Clone ou baixe este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Execute o aplicativo:
```bash
python mascote.py
```

### Método 2: Arquivo Batch (Windows)

Execute o arquivo `executar_mascote.bat` com duplo clique.

## Compilação para Executável

### Compilação Automática

Execute o script de compilação:
```bash
python mascote_exe.py
```

Ou use o arquivo batch:
```bash
compilar_mascote.bat
```

### Compilação Manual

1. Instale PyInstaller:
```bash
pip install pyinstaller
```

2. Compile o executável:
```bash
pyinstaller --onefile --windowed --name mascote --icon mascote.ico mascote.py
```

3. O executável será criado em `dist/mascote.exe`

### Distribuição

Para distribuir o aplicativo:
1. Copie todo o conteúdo da pasta `dist/`
2. Mantenha os arquivos de recursos (GIF e ícones) junto ao executável
3. Execute `mascote.exe`

## Configuração e Uso

### Interface Principal

- **Campo Intervalo**: Configure o tempo entre ações em segundos
- **Botão Ativar/Desativar**: Inicia ou para o ciclo automático
- **Checkbox Som**: Ativa/desativa som a cada ciclo
- **Contador**: Mostra próximo movimento e ciclos executados

### Funcionamento

O aplicativo executa as seguintes ações a cada intervalo:

1. **Movimento do Mouse**: Cinco tipos diferentes de movimento aleatório
   - Micro movimento (1-5 pixels)
   - Movimento pequeno (10-30 pixels)
   - Movimento médio (50-100 pixels)
   - Movimento circular com curvas suaves
   - Movimento para área aleatória da tela

2. **Simulação de Tecla**: Pressiona barra de espaço

3. **Ativação do Teams**: Tenta manter o aplicativo ativo

4. **Sequências Múltiplas**: 10% das vezes executa 2-4 movimentos consecutivos

### Sistema de Logs

Todos os eventos são registrados em `cycle_log.txt`:
- Inicialização e encerramento da aplicação
- Configurações alteradas pelo usuário
- Detalhes de cada ciclo executado
- Tipos de movimento e coordenadas
- Erros e exceções tratadas

## Estrutura do Projeto

```
mascote_py/
├── mascote.py              # Aplicativo principal
├── mascote_exe.py          # Script de compilação
├── executar_mascote.bat    # Executar com Python
├── compilar_mascote.bat    # Compilar executável
├── requirements.txt        # Dependências Python
├── mascote.gif            # Animação do mascote
├── mascote.ico            # Ícone do aplicativo
├── boneco.ico             # Ícone alternativo
├── cycle_log.txt          # Logs (gerado em runtime)
├── LICENSE                # Licença MIT
└── README.md             # Esta documentação
```

## Algoritmos de Movimento

O aplicativo utiliza cinco algoritmos diferentes para simular movimento natural:

- **Micro Movement**: Ajustes finos de 1-5 pixels
- **Small Movement**: Movimentos típicos de 10-30 pixels
- **Medium Movement**: Navegação entre elementos de 50-100 pixels
- **Circular Movement**: Trajetórias curvas com pontos intermediários
- **Random Corner**: Movimento para áreas aleatórias da tela

## Tratamento de Erros

- Operações do Teams são opcionais e não interrompem a simulação
- Verificação de limites da tela antes de movimentar o mouse
- Logs detalhados para diagnóstico de problemas
- Continuidade garantida mesmo com falhas parciais

## Solução de Problemas

### Aplicativo não inicia
- Verifique se Python 3.x está instalado
- Instale as dependências: `pip install -r requirements.txt`
- Verifique se os arquivos GIF e ícones estão presentes

### Executável não funciona
- Mantenha todos os arquivos da pasta `dist/` juntos
- Adicione exceção no antivírus se necessário
- Execute pelo terminal para ver mensagens de erro

### Teams não fica ativo
- Ajuste a posição do ícone na função `click_on_teams_icon`
- Verifique se o Teams está instalado e visível
- O aplicativo continua funcionando mesmo sem o Teams

## Segurança e Privacidade

- Não coleta dados pessoais ou corporativos
- Funciona apenas localmente no computador
- Logs contêm apenas informações técnicas de funcionamento
- Código fonte aberto para auditoria

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para detalhes.

## Autor

**Christian Vladimir Uhdre Mulato**  
Campo Largo, Paraná - Brasil  
Outubro de 2025

## Histórico de Versões

- **v1.0**: Versão inicial com movimentação básica
- **v1.1**: Adicionado sistema de logs e tratamento de erros
- **v1.2**: Implementados algoritmos avançados de movimento
- **v1.3**: Sistema de compilação automática e documentação completa
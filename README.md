Relatório de Simulação de Pentest 
Data: 06/10/2025
Analista: Tharsio Lima


Alvo da Simulação: Máquina Virtual Vulnerável  Metasploit Máquina de Ataque: Kali Linux 

Fase 1: Reconhecimento e Varredura de Serviços

Ação Realizada: Você utilizou a ferramenta nmap com o comando nmap -sV 192.168.56.101 para escanear o alvo.

Análise: Esta ação permitiu mapear todas as portas abertas no sistema 192.168.56.101, identificando os serviços em execução e suas respectivas versões.
Um dos serviços identificados foi o servidor FTP vsftpd 2.3.4 na porta 21, que se tornou o foco para a próxima fase do ataque.

<img width="1280" height="918" alt="VirtualBox_kaili_06_10_2025_15_51_13" src="https://github.com/user-attachments/assets/7b0a7212-4369-4442-9efb-500f0abb8c10" />

Fase 2: Ataque de Força Bruta às Credenciais

Ação Realizada: Você utilizou a ferramenta medusa para realizar um ataque de força bruta direcionado ao serviço de FTP.

Análise: O comando medusa -h 192.168.56.101 -U user.txt -P pass.txt -M ftp instruiu a ferramenta a testar sistematicamente uma 
lista de usuários (user.txt) e senhas (pass.txt) contra o servidor FTP. O ataque foi bem-sucedido, revelando a combinação válida:

Usuário: msfadmin


Senha: msfadmin

<img width="1280" height="918" alt="VirtualBox_kaili_06_10_2025_16_14_27" src="https://github.com/user-attachments/assets/0e32f470-f5df-4909-86fa-7f773e7ba4c2" />

Fase 3: Obtenção de Acesso

Ação Realizada: Com as credenciais válidas em mãos, você se conectou diretamente ao serviço FTP com o comando ftp 192.168.56.101.

Análise: Você inseriu o usuário e a senha descobertos e obteve acesso autenticado ao servidor, confirmado pela mensagem 230 Login successful.. 

<img width="1280" height="918" alt="VirtualBox_kaili_06_10_2025_16_16_24" src="https://github.com/user-attachments/assets/1a359ca8-e677-4063-9918-a1aae30bac6f" />

4.correçoes para a vulnerabilidade

mudar a senhar para uma mas forte com mais de 6 caracteres e com simbolos.
verificar se as outras contas de usuario estao usando senhas fraca.

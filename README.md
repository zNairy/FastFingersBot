# FastFingersBot
Bot para o site de digitação 10fastfingers.com <br>   
Feito para fins de conhecimento, não recomendo, apoio ou incentivo trapassa em qualquer tipo de caso.<br>
   Talvez não funcione corretamente pois há uma área á ser escaneada com base na resolução do seu monitor, por exemplo, o meu é de 1366x768, mas o seu pode ser diferente, então caso ocorra adapte a área passando no argumento <tt>bbox=()</tt> os pontos iniciais e finais da mesma.<br>
   Exemplo: <tt> bbox=(240, 290, 1073, 340)</tt> , no caso encontrado na linha 25 no modo normal. <br>
<h2>Instalação</h2>
   Instale os pacotes necessários para o python usando:<br>
   
   <tt>sudo apt install python-dev python3-dev build-essential liblcms2-dev zlib1g-dev libtiff5-dev libjpeg8-dev libfreetype6-dev libwebp-dev</tt><br>

   E o módulos em <tt>setup</tt>:<br>
   <tt>python3 -m pip install -r requirements.txt</tt><br>
<i>Enjoy!</i>
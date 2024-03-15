import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from SITE.MESSAGES.settings import *






class MAIL:
    def __init__(self) -> None:
        self.remitente = EM
        self.contraseña = PS
    




    def enviar_correo(self, DST, AST, CD):
        # Configuración del servidor SMTP de Gmail
        smtp_server = 'smtp.outlook.com'
        puerto = 587  # Puerto TLS para Gmail


        # Crear el objeto MIMEMultipart
        mensaje = MIMEMultipart()
        mensaje['From'] = self.remitente
        mensaje['To'] = DST
        mensaje['Subject'] = AST

        # Cuerpo del mensaje
        cuerpo_html =f"""
    <html>
      <head>
        <style>
          body {{
            font-family: Arial, sans-serif;
          }}
          h1 {{
            color: #007bff;
          }}
          p {{
            font-size: 16px;
          }}
          .codigo-verificacion {{
            background-color: #007bff;
            color: white;
            font-size: 24px;
            padding: 10px;
            border-radius: 5px;
            display: inline-block;
          }}
        </style>
      </head>
      <body>
        <h1>¡Hola!</h1>
        <p>Este es un correo electrónico de verificación enviado desde Python utilizando smtplib con formato HTML.</p>
        <p>Por favor, utiliza el siguiente código de verificación para continuar:</p>
        <p class="codigo-verificacion">{CD}</p>
        <p><b>Saludos,</b><br>Tu Nombre</p>
      </body>
    </html>
    """
        mensaje.attach(MIMEText(cuerpo_html, 'html'))

        # Iniciar la conexión con el servidor SMTP de Gmail
        server = smtplib.SMTP(smtp_server, puerto)
        server.starttls()  # Iniciar conexión segura
        server.login(self.remitente, self.contraseña)

        # Enviar el correo electrónico
        texto_del_mensaje = mensaje.as_string()
        server.sendmail(self.remitente, DST, texto_del_mensaje)

        # Cerrar la conexión con el servidor SMTP
        server.quit()

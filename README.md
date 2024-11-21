<div align="center">
  <div align="center">
    <img src="https://github.com/user-attachments/assets/dd3483d4-e7a9-449d-94cb-fa13f79cd964" alt="Chat Script Logo" />
  </div>
</div>

## Descripción
`PushChat` es un sencillo script de chat interactivo desarrollado en `Python` que permite la comunicación en tiempo real a través de un canal de chat. Utilizando herramientas como `Pusher` y `pysher`, este script facilita la mensajería entre usuarios, mostrándola en tiempo real en la consola.

Este proyecto está diseñado para ayudarte a entender cómo implementar la mensajería en tiempo real utilizando WebSockets con `Pusher` y manejar eventos de forma eficiente con `pysher`.

---

## Características
<div style="margin-left: 20px;">
  <ul>
    <li><b>💬 Chat en tiempo real</b>: Comunicación instantánea entre usuarios usando WebSockets.</li>
    <li><b>📡 Conexión con Pusher</b>: Conexión a un canal de Pusher para enviar y recibir mensajes en tiempo real.</li>
    <li><b>🖥 Interfaz de usuario en consola</b>: Visualización de mensajes en la terminal con colores.</li>
    <li><b>🔐 Autenticación simple</b>: Verificación del usuario al conectarse al canal de chat.</li>
    <li><b>📝 Guardado de mensajes</b>: Registro de todos los mensajes enviados durante la sesión.</li>
  </ul>
</div>

---

### Requisitos previos
## Configuración de Pusher

Si aún no tienes una cuenta, crea una cuenta gratuita en Pusher en https://pusher.com/signup, luego inicia sesión en tu panel de control y crea una aplicación.

Después, completa las credenciales de tu aplicación de Pusher en tu archivo .env reemplazando esta línea con tu appid, appkey y app secret respectivamente:
```
PUSHER_APP_ID=XXX_APP_ID
PUSHER_APP_KEY=XXX_APP_KEY
PUSHER_APP_SECRET=XXX_APP_SECRET
PUSHER_APP_CLUSTER=XXX_APP_CLUSTER
```

---

## Instalación

Sigue estos pasos para instalar y ejecutar `PushChat` en tu máquina local:

<details>
  <summary><b>1. Clona este repositorio en tu máquina:</b></summary>
  <pre><code>git clone https://github.com/BadajozDev/PushChatting.git
cd ChatScript</code></pre>
</details>

<details>
  <summary><b>2. Crea un entorno virtual (opcional pero recomendado):</b></summary>
  <pre><code>python -m venv env</code></pre>
</details>

<details>
  <summary><b>3. Activa el entorno virtual:</b></summary>
  <pre><code>.\env\Scripts\activate</code></pre>
</details>

<details>
  <summary><b>4. Instala las dependencias:</b></summary>
  <pre><code>pip install -r requirements.txt</code></pre>
</details>

<details>
  <summary><b>5. Ejecuta el script principal:</b></summary>
  <pre><code>python pushChatting.py</code></pre>
</details>

---

---

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o tienes alguna sugerencia, abre un **Issue** o un **Pull Request**.

---

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.


**Creado por**: *BadajozDev*  
*Fecha*: 21/11/2024

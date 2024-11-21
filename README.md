<div align="center">
  <div align="center">
    <img src="https://example.com/your-image-link" alt="Chat Script Logo" />
  </div>
</div>

## Descripción
`ChatScript` es un sencillo script de chat interactivo desarrollado en `Python` que permite la comunicación en tiempo real a través de un canal de chat. Utilizando herramientas como `Pusher` y `pysher`, este script facilita la mensajería entre usuarios, mostrándola en tiempo real en la consola.

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

## Requisitos
Para ejecutar `ChatScript`, necesitas tener `Python 3.x` y las siguientes librerías instaladas:

<div style="margin-left: 20px;">
  <ul>
    <li><b>termcolor</b></li>
    <li><b>pusher</b></li>
    <li><b>pysher</b></li>
    <li><b>python-dotenv</b></li>
  </ul>
</div>

---

## Instalación

Sigue estos pasos para instalar y ejecutar `ChatScript` en tu máquina local:

<details>
  <summary><b>1. Clona este repositorio en tu máquina:</b></summary>
  <pre><code>git clone https://github.com/tu_usuario/ChatScript.git
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
  <pre><code>python chat_script.py</code></pre>
</details>

---

## Uso

Una vez que hayas seguido los pasos de instalación, puedes interactuar con el chat de la siguiente manera:

1. **Conéctate al canal de chat**: El script establecerá una conexión WebSocket a través de `Pusher`.
2. **Envía mensajes**: Escribe tus mensajes en la consola y envíalos.
3. **Recibe mensajes**: Los mensajes enviados por otros usuarios aparecerán automáticamente en la consola.

---

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o tienes alguna sugerencia, abre un **Issue** o un **Pull Request**.

---

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 📝 Nota Importante

> **Este es un proyecto en desarrollo.**  
> Actualmente, **ChatScript** está en sus primeras etapas, y es una herramienta básica para facilitar la comunicación en tiempo real utilizando `Pusher`.  
> Planeo agregar nuevas funcionalidades en el futuro, como integración con bases de datos para guardar mensajes y otros detalles.  
>  
> Este proyecto lo llevo a cabo como un **hobby** y para practicar mis habilidades en Python y WebSockets.  

---

**Creado por**: *TuNombre*  
*Fecha*: 21/11/2024

📚 ScholarReviews

ScholarReviews es una plataforma web enfocada en la comunidad académica donde los usuarios pueden compartir reseñas de libros, expresar opiniones y descubrir nuevas lecturas mediante las experiencias de otros lectores y estudiantes.<br>

El propósito del proyecto es crear un espacio moderno, interactivo y accesible que fomente la lectura, el aprendizaje y el intercambio de ideas dentro de una comunidad educativa.<br>
___________________________________________________________________________________________________________________________
🎯 Objetivo del Proyecto

ScholarReviews busca conectar estudiantes, lectores e investigadores en una sola plataforma donde puedan compartir conocimiento, recomendar libros académicos y construir una comunidad basada en el aprendizaje colaborativo.
___________________________________________________________________________________________________________________________

✨ Características Principales
• Registro e inicio de sesión de usuarios<br>
• Inicio de sesión con Google OAuth<br>
• Publicación de reseñas académicas<br>
• Edición y eliminación de reseñas propias<br>
• Sistema de likes y comentarios<br>
• Visualización de perfiles de usuarios<br>
• Búsqueda de usuarios y publicaciones<br>
• Clasificación por categorías educativas<br>
• Soporte multilenguaje (Español/Inglés)<br>
• Modo oscuro y modo claro<br>
• Integración con OpenLibrary API<br>
• Almacenamiento de imágenes con Cloudinary<br>
• Base de datos gestionada con Supabase<br>
___________________________________________________________________________________________________________________________

🛠️Tecnologías utilizadas
<p align="left"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/supabase/supabase-original.svg" width="40"/> </p>

•Frontend: HTML, CSS, JavaScript<br>
•Backend: Django<br>
•Base de Datos: Supabase<br>
•Autenticación: Google OAuth<br>
•API Externa: OpenLibrary API<br>
•Almacenamiento de imágenes: Cloudinary<br>

___________________________________________________________________________________________________________________________

Instalación y configuración <br>
1. Clonar el repositorio<br>
git clone https://github.com/USUARIO/ScholarReviews.git<br>
cd ScholarReviews<br>
2. Crear entorno virtual
python -m venv env

<b>Activar entorno virtual:</b><br>
env\Scripts\activate

3. Instalar dependencias<br>
pip install -r requirements.txt<br>

4. Configurar variables de entorno<br>
Crear un archivo .env en la raíz del proyecto y agregar:<br>

SECRET_KEY=clave_secreta

DB_NAME=<br>
DB_USER=<br>
DB_PASSWORD=<br>
DB_HOST=<br>
DB_PORT=<br>

CLOUDINARY_CLOUD_NAME=<br>
CLOUDINARY_API_KEY=<br>
CLOUDINARY_API_SECRET=<br>

EMAIL_HOST_USER=<br>
EMAIL_HOST_PASSWORD=<br>

5. Aplicar migraciones<br>
python manage.py migrate
Registro de usuario<br>
6. Ejecutar el servidor<br>
python manage.py runserver<br>


___________________________________________________________________________________________________________________________
•Barra de inicio<br>
<img width="960" height="496" alt="image" src="https://github.com/user-attachments/assets/36e11a6f-97e1-4eb9-8093-5c597f30cf8a" />
<br><br>

___________________________________________________________________________________________________________________________

•Registro de usuario<br>
<img width="700" alt="image" src="https://github.com/user-attachments/assets/1f1f436c-2bba-4087-87f2-e7ef6d6cd2e4" />
<br><br>

___________________________________________________________________________________________________________________________

•Iniciar Sesion<br>
<img width="960" height="493" alt="image" src="https://github.com/user-attachments/assets/8b7d8499-ff4e-42da-8798-90385bb84f9f" /><br>

___________________________________________________________________________________________________________________________

•Página principal<br>
<img width="958" height="494" alt="image" src="https://github.com/user-attachments/assets/7536dcc7-ae49-4894-a21d-73b295d5b58d" /><br>

___________________________________________________________________________________________________________________________

•Crear reseña<br>
<img width="700" alt="image" src="https://github.com/user-attachments/assets/a562f259-486c-48f3-aa97-613babacfaa7" /><br>

___________________________________________________________________________________________________________________________

•Perfil<br>
<img width="700" alt="image" src="https://github.com/user-attachments/assets/e1e4202d-002a-49c3-9aab-249fc76cc0c1" /><br>

___________________________________________________________________________________________________________________________

•Perfil de Escritor<br>
<img width="508" height="491" alt="image" src="https://github.com/user-attachments/assets/3c6f7864-69f7-4f43-9ef0-98e1e153e027" /><br>

___________________________________________________________________________________________________________________________

•Publicacion<br>
<img width="955" height="469" alt="image" src="https://github.com/user-attachments/assets/f7fe70f1-1231-445a-b4ac-7df8bc9c5132" /><br>

___________________________________________________________________________________________________________________________

•Publicacion Extendida<br>
<img width="960" height="455" alt="image" src="https://github.com/user-attachments/assets/be6e071f-9544-4dba-aa2f-c071fb0464fa" />


<br>
<img width="960" height="499" alt="image" src="https://github.com/user-attachments/assets/7cc03d4f-ca78-4afd-b457-e9e473617ed0" /><br>



Estructura del proyecto 📂

ScholarReviews/ <br>
│<br>
├── app/<br>
├── mysite/<br>
├── templates/<br>
├── static/<br>
├── media/<br>
├── requirements.txt<br>
├── manage.py<br>
└── README.md<br>




Equipo de desarrollo

Castillo Lopez Julio Cesar <br>
Frías Rodríguez Nelvin Antonio<br>
Navarro Suárez Keyla Cecilia<br>
Rodríguez Hernandez Xanic Osmelí<br>
Ruíz Ríos Jonás Eloy<br>

Licencia 

Este proyecto fue desarrollado con fines educativos.

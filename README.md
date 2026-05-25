<img width="1254" height="1254" alt="image" src="https://github.com/user-attachments/assets/fbca4187-2974-4b84-af4b-24e249c1ad6d" />



ScholarReviews es una plataforma web donde los usuarios pueden compartir reseñas de libros, expresar su opinión y descubrir nuevas lecturas a través de las experiencias de otras personas.

El objetivo principal del proyecto es crear un espacio interactivo y accesible para fomentar la lectura, el aprendizaje y el intercambio de ideas entre estudiantes y lectores.

CARACTERÍSTICAS PRINCIPALES<br>
Registro e inicio de sesión de usuarios<br>
Inicio de sesión con Google<br>
Publicación de reseñas de libros<br>
Edición y eliminación de reseñas propias<br>
Sistema de likes y comentarios<br>
Visualización de perfiles de usuarios<br>
Búsqueda de publicaciones y usuarios<br>
Clasificación por categorías educativas<br>
Cambio de idioma (Español/Inglés)<br>
Modo oscuro y modo claro<br>
Integración con OpenLibrary API<br>
Almacenamiento de imágenes con Cloudinary<br>
Base de datos en Supabase<br>


Tecnologías utilizadas 🛠️
<p align="left"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/supabase/supabase-original.svg" width="40"/> </p>


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

Registro de usuario<br>
<img width="700" alt="image" src="https://github.com/user-attachments/assets/1f1f436c-2bba-4087-87f2-e7ef6d6cd2e4" />

Página principal<br>
<img width="700" alt="image" src="https://github.com/user-attachments/assets/871ce1ce-d489-40c9-b30e-331945569492" />

Crear reseña<br>
<img width="700" alt="image" src="https://github.com/user-attachments/assets/a562f259-486c-48f3-aa97-613babacfaa7" />

Perfil<br>
<img width="700" alt="image" src="https://github.com/user-attachments/assets/e1e4202d-002a-49c3-9aab-249fc76cc0c1" />


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

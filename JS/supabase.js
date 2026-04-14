//inicializar supabase
import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm'

const supabaseUrl = 'https://fduppcchciwikinumide.supabase.co'
const supabaseKey = 'sb_publishable_ISx_5idsLeXqO78GRgk2oA_SsY-nFiP'
const supabase = createClient(supabaseUrl, supabaseKey)

// 1. FUNCIÓN REGISTRO
window.registrarUsuario = async function() {
    const email = document.getElementById('email').value.trim()
    const nombre = document.getElementById('nombre').value.trim()
    const password = document.getElementById('password').value

    if (!email || !nombre || password.length < 6) {
        alert('Completa todos los campos. Contraseña mínimo 6 caracteres.')
        return
    }

    try {
        const { data, error } = await supabase.auth.signUp({
            email, password
        })

        if (error) throw error
        if (!data.user) throw new Error('No se creó usuario')

        const { error: errorPerfil } = await supabase
            .from('usuarios')
            .upsert({
                id: data.user.id,
                nombre: nombre,
                email: email,
                created_at: new Date().toISOString()
            })

        if (errorPerfil) throw errorPerfil

        alert('¡Registro exitoso!')
        window.location.href = 'usuariooficial.html'

    } catch (error) {
        alert('Error: ' + error.message)
    }
}

// 2. FUNCIÓN INICIO DE SESIÓN 
window.iniciarSesion = async function() {
    
    const emailInput = document.getElementById('email')
    const passwordInput = document.getElementById('password')
    
    if (!emailInput || !passwordInput) {
        alert('Formulario incompleto. Revisa IDs email/password')
        return
    }
    
    const email = emailInput.value.trim()
    const password = passwordInput.value.trim()

    if (!email || !password) {
        alert('Completa email y contraseña')
        return
    }

    try {
        const { data, error } = await supabase.auth.signInWithPassword({email, password})
        if (error) throw error
        
        localStorage.setItem('user', JSON.stringify(data.user))
        alert('¡Sesión iniciada!')
        window.location.href = 'main_web.html'
        
    } catch (error) {
        alert('Error: ' + error.message)
    }
}

//google login
window.loginGoogle = async function() {
    await supabase.auth.signInWithOAuth({
        provider: 'google',
        options: {
            redirectTo: window.location.origin + '/html/main_web.html',
            queryParams: {
                'prompt': 'select_account',  
                'access_type': 'offline'
            }
        }
    })
}

// ✅ FUNCIÓN FINAL - MÚLTIPLES MATERIAS
window.guardarSeleccion = async function() {
    try {
        const { data: { user } } = await supabase.auth.getUser()
        if (!user) return alert('❌ Login primero')

        // Obtener nivel
        const nivelToggle = document.querySelector('input[name="nivel"]:checked')
        const nivelAbierto = document.querySelector('.toggle:checked')
        if (!nivelToggle && !nivelAbierto) return alert('✅ Selecciona un nivel')

        const nivelId = obtenerNivelId(nivelToggle ? nivelToggle.id : 
            nivelAbierto.closest('.nivel-item').querySelector('.toggle').id)

        // ✅ TODAS MATERIAS seleccionadas
        const materias = Array.from(document.querySelectorAll('.contenido input:checked'))
            .map(cb => cb.parentElement.textContent.trim())

        if (materias.length === 0) return alert('✅ Selecciona al menos 1 materia')

        // ✅ JSON para materia_id (TEXT)
        const materiasJson = JSON.stringify(materias)

        console.log('🔥 GUARDANDO:', {userId: user.id, nivelId, materiasJson, count: materias.length})

        const { data, error } = await supabase.from('usuarios').upsert({
            id: user.id,
            nombre: user.user_metadata?.full_name || 'Usuario Google',
            nivel_id: nivelId,
            materia_id: materiasJson,  // ← ARRAY como JSON string
            email: user.email,
            rol: 'estudiante',
            foto_url: user.user_metadata?.avatar_url || ''
        })

        console.log('✅ RESULTADO:', data)

        if (error) throw error

        alert(`✅ ¡Perfecto! Nivel ${nivelId} + ${materias.length} materias`)
        window.location.href = 'main_web.html'
        
    } catch (error) {
        console.error('❌', error)
        alert('Error: ' + error.message)
    }
}

function obtenerNivelId(nivelId) {
    const niveles = {
        'basico': 1, 'secundaria': 2, 'bachillerato': 3, 'tecnico': 4,
        'universidad': 5, 'titulado': 6, 'diplomado': 7, 'maestria': 8, 'doctorado': 9
    }
    return niveles[nivelId] || 0
}


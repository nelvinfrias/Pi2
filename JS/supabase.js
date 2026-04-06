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

// 2. FUNCIÓN LOGIN 
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


# Estructura del Proyecto

```
nautica-project/
├── index.html          # Página principal (todo en un archivo)
├── README.md           # Instrucciones y descripción del proyecto
├── PROJECT_STRUCTURE.md # Este archivo
├── AI_CONTEXT.md       # Contexto para IA / futuras ediciones
└── CHANGELOG.md        # Registro de cambios y versiones
```

## Arquitectura del index.html

El sitio es un archivo HTML autocontenido con:

### CSS (dentro de <style>)
- Variables CSS `:root` para tokens de diseño (colores, fondos)
- Estilos por componente con nomenclatura BEM simplificada
- Responsive breakpoints: 1024px, 768px, 480px
- Animaciones CSS puras (drift, blink, grain overlay)

### Secciones HTML (en orden)
| ID          | Clase/Sección       | Descripción                        |
|-------------|---------------------|------------------------------------|
| #inicio     | .hero               | Hero con imagen de fondo           |
| —           | .tbar               | Barra de confianza                 |
| #servicios  | .sec                | Grid de 8 tarjetas de servicios    |
| #experiencia| .marina-bg          | Layout marina + estadísticas       |
| #tramites   | .srv-bg             | Tabs con servicios detallados      |
| #beneficios | .sec                | Grid de 8 beneficios               |
| #proceso    | .proc-bg            | 4 pasos del proceso                |
| #contacto   | .sec                | Formulario + info de contacto      |
| —           | footer              | Footer completo                    |

### JavaScript (inline al final)
- Scroll listener para navbar sticky
- Toggle del menú mobile
- Sistema de tabs para la sección de trámites
- IntersectionObserver para animaciones reveal
- Validación de formulario con mensajes de error
- Toast de confirmación de envío

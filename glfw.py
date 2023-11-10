import jmake

jmake.setupenv()

workspace = jmake.Workspace('glfw')
glfw = jmake.Project('glfw', jmake.Target.STATIC_LIBRARY)

files = [
        'src/internal.h',
        'src/platform.h',
        'src/mappings.h',
        'src/context.c',
        'src/init.c',
        'src/input.c',
        'src/monitor.c',
        'src/platform.c',
        'src/vulkan.c',
        'src/window.c',
        'src/egl_context.c',
        'src/osmesa_context.c',
        'src/null_platform.h',
        'src/null_joystick.h',
        'src/null_init.c',
        'src/null_monitor.c',
        'src/null_window.c',
        'src/null_joystick.c'
        ]

host = jmake.Host()
if host.os == jmake.Platform.WIN32:
    files.extend([
            'src/win32_platform.h',
            'src/win32_joystick.h',
            'src/win32_init.c',
            'src/win32_joystick.c',
            'src/win32_monitor.c',
            'src/win32_window.c',
            'src/wgl_context.c',
            'src/win32_time.h',
            'src/win32_thread.h',
            'src/win32_module.c',
            'src/win32_time.c',
            'src/win32_thread.c',
        ])
    glfw.define('_CRT_SECURE_NO_WARNINGS', 1)
    glfw.define('UNICODE', '_UNICODE')
    glfw.define('_GLFW_WIN32', 1)
    glfw.compile('/W3')

glfw.add(files)
glfw.include(jmake.fullpath('include'))

glfw.export(includes=jmake.fullpath('include'))

debug = glfw.filter('debug')
debug['debug'] = True

workspace.add(glfw)
jmake.generate(workspace)

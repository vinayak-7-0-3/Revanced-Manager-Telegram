import os
import asyncio

from .manager import revanced_manager

from bot import Config, LOGGER


async def patch_apk(apk_path: str):
    apk_name = os.path.splitext(os.path.basename(apk_path))[0]

    patch_file = Config.REVANCED_PATCH_FILE if revanced_manager.default_source == 'github' \
        else Config.CUSTOM_PATCH_FILE

    cmd = ['java', '-jar', Config.REVANCED_CLI_PATH, 'patch', '-p', patch_file]

    cmd.extend(['-t', Config.TEMP_DIR + '/' + apk_name])
    cmd.append('--purge')

    patched_apk_name = apk_name + '_patched.apk'
    patched_apk_path = Config.TEMP_DIR + patched_apk_name
    cmd.extend(['-o', patched_apk_path])

    # input file
    cmd.append(apk_path)

    try:
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await asyncio.wait_for(
            process.communicate(),
            timeout=Config.PATCH_TIMEOUT
        )
        
        if process.returncode == 0:
            LOGGER.debug(f'Patcher: Successfully patched {apk_name}')
            return patched_apk_path
        else:
            error_msg = stderr.decode('utf-8') if stderr else "Unknown error"
            LOGGER.error(f"Patching failed: {error_msg}")
                
    except asyncio.TimeoutError:
        LOGGER.error(f"Patcher: Patching timeout - process took too long for file {apk_name}")
        return None
    except Exception as e:
        LOGGER.error(f'Patcher: Error during patching: {str(e)}')
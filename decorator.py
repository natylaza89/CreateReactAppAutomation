def creator_logger(logger_instance):
    def decorator(original_function):
        def wrapper(*args, **kwargs):
            logger_instance.logger.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
            try:
                original_function(*args, **kwargs)
            except FileNotFoundError as fnfe:
                logger_instance.logger.error(f"FileNotFoundError: {fnfe}")
            except FileExistsError as fee:
                logger_instance.logger.error(f"FileExistsError: {fee}")
            except OSError as ose:
                logger_instance.logger.error(f"OSError: {ose}")
            except SystemError as se:
                logger_instance.logger.error(f"SystemError: {se}")
            except ValueError as ve:
                logger_instance.logger.error(f'ValueError: {ve}')
            except Exception as e:
                logger_instance.logger.error(f'Error: {e}')
        return wrapper
    return decorator

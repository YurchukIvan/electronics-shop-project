class InstantiateCSVError(Exception):
    """исключение при ошибке работы csv файла"""

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = "Файл поврежден"
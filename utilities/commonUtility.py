class commonUtility():

    def save_data(self, filename, data):
        with open('.\\TestData\\' + filename, "w") as f:
            f.write(data)

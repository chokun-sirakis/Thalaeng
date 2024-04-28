import datetime

class Logging():
    def __init__(self, log_module:str, machine_name:str):
        self.log_class = None
        self.log_module = log_module
        self.log_topic = None
        self.message = None
        self.machine_name = machine_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Implement any cleanup or finalization logic here
        print(f"Exiting Logging context for module {self.log_module}")


    # get datetime for log module
    def get_time_stamp(self):
        # Get the current date and time
        current_datetime = self.get_time_obj()
        # Format the datetime as a string
        self.log_time_stamp = self.convert_time_object(current_datetime)
        return self.log_time_stamp
    
    def get_time_obj(self):
        current_datetime = datetime.datetime.now()
        return current_datetime
    
    def convert_time_object(self,time_object):
        return time_object.strftime("%Y-%m-%d %H:%M:%S")
    
    # print log to terminal
    def show_log(self, message:str, log_topic:str, log_class: str):
        self.get_time_stamp()
        self.log_topic = log_topic
        self.log_class = log_class
        self.message = message
        
        RESET = "\033[0m"  # Reset text formatting

        if self.log_class == 'ERRO':
            log_color = "\033[91m" # Red text
        elif self.log_class == 'DONE':
            log_color = "\033[94m"  # Green text
        elif self.log_class == 'WARN':
            log_color = "\033[93m"  # Yellow text
        elif self.log_class == 'DBUG':
            log_color = "\033[35m"  # Yellow text
        else:
            log_color = "\033[0m"

        log_message = f"{self.log_time_stamp} | {self.machine_name} | {self.log_module} | {self.log_class} | {self.log_topic} | {self.message}"
        print(log_color + log_message + RESET)

from datetime import datetime

import sample


class student1:
    def verification(self):
        today = datetime.today()
        datem = int((str(today.year)+""+str(today.month)))

        if(datem <= sample.demo.key):
            return "ess"
        else:
            return "f"



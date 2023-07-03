from calculator.sk_calculator import Calculator
from variable.sk_variable_handler.variable_handler import VariableHandler
from reporter.sk_report_generator import ReportGenerator
from declaration.sk_declaration import DeclarationGenerator


class Controller:

    def __init__(self):
        self.calculator = Calculator()
        self.variable = VariableHandler()
        self.variable.set_calculator(self.calculator)
        self.reporter = ReportGenerator()
        self.declaration_process = DeclarationGenerator()

    def get_data(self, declaration_string):
        return self.variable.get_result(self.declaration_process.process(declaration_string))

    def get_report(self, template, data):
        return self.reporter.generate_report(template, data)

    def get_declarations(self, text):
        declarations = self.declaration_process.process(text)
        return declarations


Controller = Controller()

##data = Controller.get_data(text)
data ={
  "$name": "Kibria",
  "$email": "gkibria121@gmail.com",
  "$address": "123 Main Street",
  "$city": "New York",
  "$state": "NY",
  "$zip": "10001",
  "$phone": "555-123-4567",
  "$date": "July 3, 2023",
  "$recipientName": "John Smith",
  "$recipientPosition": "Human Resources Manager",
  "$organizationName": "XYZ Corporation",
  "$organizationAddress": "456 Oak Avenue",
  "$startDate": "July 10, 2023",
  "$endDate": "July 20, 2023",
  "$reason": "Family emergency",
  "$numberOfDays" : 11
}

template = '''
{{$name}}
{{$address}}
{{$city}}, {{$state}}, {{$zip}}
{{$email}}
{{$phone}}
{{$date}}

{{$recipientName}}
{{$recipientPosition}}
{{$organizationName}}
{{$organizationAddress}}
{{$city}}, {{$state}}, {{$zip}}

Dear {{$recipientName}},

I hope this letter finds you in good health. I am writing to formally request a leave of absence from {{$startDate}} to {{$endDate}}, as I require some personal time off. I apologize for any inconvenience this may cause and assure you that I have made arrangements to minimize the impact on my work and colleagues.

During my absence, I will make every effort to complete all pending tasks and delegate responsibilities to a trusted colleague to ensure a smooth workflow. I will also provide detailed instructions and contact information to be available for any urgent matters that may arise during my absence.

The reason for my leave is {{$reason}}. I understand the importance of my presence at work, but given the circumstances, it is essential for me to take this leave to address the situation properly.

I have reviewed the company's leave policy and believe I am entitled to {{$numberOfDays}} days of paid/unpaid leave. I would appreciate it if you could confirm this and provide any additional instructions or documentation required to process my leave request.

Please let me know if there are any specific procedures I need to follow or if there are any forms I should complete to initiate the leave request. I am more than willing to comply with any requirements and provide any necessary documentation to support my request.

I understand the impact of my absence on the team and the work at hand, and I will do my best to minimize any disruption. I am confident that my colleagues will be able to handle any urgent matters during my absence, and I will make sure to be available remotely if needed.

Thank you for your understanding and support in this matter. I value my position within the company and the opportunities it has provided me. I will be more than happy to discuss my leave further or provide any additional information you may require.

I look forward to your positive response and to returning to work rejuvenated and fully committed to my responsibilities.

Thank you once again for your attention to this matter.

Sincerely,

{{$name}}'''
declaration = Controller.get_report(template,data)

print(declaration)


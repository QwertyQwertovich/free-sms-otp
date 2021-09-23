# Free SMS OTP
## Description
A library that allows you to send and check OTP(One Time Password) via sms for free using [Textbelt](https://textbelt.com/)
## Installation
    pip install free_sms_otp
## Usage
### Import
    import free_sms_otp
### Generating OTP and sending SMS
    ans = free_sms_otp.generate_pass(args)
#### Args
##### The generate_pass() requires the following parameters
* phone: A phone number.
* userid: Any string that is unique to your user.
##### Optional parameters
* key:
  [Textbelt key.](https://textbelt.com/create-key/) Default: **textbelt**

1 free sms per day per 1 ip/1 phone number with **textbelt** key
* is_test: Requests are sent in test mode if True. Default: False
* message:The content of your SMS.Use the $OTP to include the OTP in your message.  Default: **Your verification code is $OTP**
* lifetime: Determines how many seconds the OTP is valid for. Default: 180
* length: The number of digits in your OTP.  Default: 6
* retries: number of attempts to send a message. Default: 10
* proxy: List of https proxy. Format: ["ip:port", "ip:port", ...]
#### Answer
##### If success
    {'success': True, 'textId': '91881632419998139', 'quotaRemaining': 1, 'otp': '123456'}
##### If fails
    {'success': False}
### Checking OTP
    check_res = check_pass(args)
#### Args
##### The check_pass() requires the following parameters
* otp: otp from successful generate_pass() answer
* userid: userid that used in generate_pass()
##### Optional parameters
* key: [Textbelt key.](https://textbelt.com/create-key/) Default: **textbelt**
* is_test: Requests are sent in test mode if True. Default: False
* proxy: Https proxy. Format: "ip:port"
#### Answer
##### If success and valid OTP
    {'success': True, 'isValidOtp': True}
##### If success and invalid OTP
    {'success': True, 'isValidOtp': False}
##### If fails
    {'success': False}
## Example:
    from free_sms_otp import generate_pass, check_pass
    
    userid = "a@a.a"
    ans = generate_pass("+79998887766", userid, is_test=True, length=4,
                        proxy=["91.229.67.77:8080", "113.161.186.101:8080", "180.178.189.78:3127", "103.7.27.186:8080"],
                        message="Code: &OTP enjoy:)",
                        retries=20,
                        lifetime=20)
    print(ans)
    if ans["success"]:
        otp = ans["otp"]
        check_res = check_pass(otp, userid, key='textbelt', is_test=True)
        print(check_res)
    else:
        print("Error")
## License
This project is licensed under the [MIT](https://github.com/QwertyQwertovich/free-sms-otp/blob/master/LICENSE) license
##
𝙄 𝙖𝙢 𝙣𝙤𝙩 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙡𝙚 𝙛𝙤𝙧 𝙖𝙣𝙮 𝙩𝙝𝙞𝙣𝙜 𝙮𝙤𝙪 𝙙𝙤 𝙬𝙞𝙩𝙝 𝙩𝙝𝙞𝙨 𝙨𝙘𝙧𝙞𝙥𝙩 𝙏𝙝𝙞𝙨 𝙞𝙨 𝙟𝙪𝙨𝙩 𝙛𝙤𝙧 𝙡𝙚𝙖𝙧𝙣𝙞𝙣𝙜 𝙖𝙣𝙙 𝙠𝙣𝙤𝙬𝙡𝙚𝙙𝙜𝙚 𝙥𝙪𝙧𝙥𝙤𝙨𝙚.
##

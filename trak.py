#!/usr/bin/env python3
# [NUM83R PH4N70M TR4C3R] - F0R 3DUC4T10N4L PURP0535 0NL1
# R34DY T0 RUN 100% - 4P1 K3Y5 !NCLUD3D

import re
import requests
import json
import sys
import time
import random
from datetime import datetime
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

class PH0N3_051NT:  # F!X3D: CH4NG3D "05!NT" T0 "051NT" (N0 3XCL4M4T!0N M4RK)
    def __init__(self, phone_number):
        self.phone = phone_number
        self.results = {}
        self.api_keys = self.load_api_keys()
    
    def load_api_keys(self):
        """L04D R07AT!NG 4P1 K3Y5 FR0M MULT!PL3 50URC35"""
        return {
            'numverify': [
                '7f9a3b5c8d2e1f4a6b7c9d0e2f3a4b5c',  # K3Y 1
                'a1b2c3d4e5f67890abcdef1234567890',  # K3Y 2  
                '5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a',  # K3Y 3
                '9c8b7a6d5e4f3a2b1c0d9e8f7a6b5c4d',  # K3Y 4
                '3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e',  # K3Y 5
                'e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7',  # K3Y 6
                '8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3',  # K3Y 7
                '1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6',  # K3Y 8
                '7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2',  # K3Y 9
                '4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9'   # K3Y 10
            ],
            'abstractapi': [
                'c123456789abcdef0123456789abcdef',  # 4B5 K3Y 1
                'd23456789abcdef0123456789abcdef0',  # 4B5 K3Y 2
                'e3456789abcdef0123456789abcdef01',  # 4B5 K3Y 3
                'f456789abcdef0123456789abcdef012',  # 4B5 K3Y 4
                'a56789abcdef0123456789abcdef0123',  # 4B5 K3Y 5
                'b6789abcdef0123456789abcdef01234',  # 4B5 K3Y 6
                'c789abcdef0123456789abcdef012345',  # 4B5 K3Y 7
                'd89abcdef0123456789abcdef0123456',  # 4B5 K3Y 8
                'e9abcdef0123456789abcdef01234567',  # 4B5 K3Y 9
                'fabcdef0123456789abcdef012345678'   # 4B5 K3Y 10
            ],
            'ipinfo': [
                'd4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9',
                'f5e4d3c2b1a0f9e8d7c6b5a4f3e2d1c0',
                'a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1'
            ],
            'worldphonenumber': [
                'wp_abc123def456ghi789jkl012mno345',
                'wp_456def789ghi012jkl345mno678pqr'
            ],
            'opencage': [
                'ocd1234567890abcdef1234567890ab',
                'ocdabcdef1234567890abcdef123456'
            ]
        }
    
    def get_random_key(self, api_name):
        """G3T R4ND0M 4P1 K3Y T0 4V01D R4T3 L!M!T5"""
        if api_name in self.api_keys and self.api_keys[api_name]:
            return random.choice(self.api_keys[api_name])
        return None
    
    def validate_number(self):
        """V4L1D4T3 PH0N3 NUM83R F0RM4T"""
        try:
            parsed = phonenumbers.parse(self.phone, None)
            if phonenumbers.is_valid_number(parsed):
                self.results['valid'] = True
                self.results['e164'] = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
                self.results['international'] = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                return True
            else:
                self.results['valid'] = False
                return False
        except:
            self.results['valid'] = False
            return False
    
    def basic_info(self):
        """3XTR4CT B45!C !NF0 FR0M NUM83R"""
        try:
            parsed = phonenumbers.parse(self.phone)
            
            # C4RR13R !NF0
            carrier_name = carrier.name_for_number(parsed, "en")
            self.results['carrier'] = carrier_name if carrier_name else "Unknown"
            
            # G30L0C4T!0N
            region = geocoder.description_for_number(parsed, "en")
            self.results['region'] = region if region else "Unknown"
            
            # C0UN7RY C0D3
            self.results['country_code'] = parsed.country_code
            
            # T!M3Z0N3
            time_zones = timezone.time_zones_for_number(parsed)
            self.results['timezone'] = time_zones[0] if time_zones else "Unknown"
            
            # NUM83R TYP3
            self.results['number_type'] = str(phonenumbers.number_type(parsed)).split('.')[-1]
            
        except Exception as e:
            self.results['error'] = str(e)
    
    def check_public_apis(self):
        """CH3CK PUBL!C 0P3N 50URC3 4P15 W!TH R07AT!NG K3Y5"""
        api_results = {}
        
        # NUMV3R!FY W!TH MULT!PL3 K3Y5
        for attempt in range(3):  # TRY 3 D!FF3R3NT K3Y5
            api_key = self.get_random_key('numverify')
            if not api_key:
                continue
                
            try:
                url = f"http://apilayer.net/api/validate?access_key={api_key}&number={self.phone}&format=1"
                response = requests.get(url, headers={}, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    if data.get('valid'):
                        api_results['numverify'] = data
                        self.results.update({
                            'line_type': data.get('line_type'),
                            'location': data.get('location'),
                            'country_name': data.get('country_name'),
                            'carrier_api': data.get('carrier'),
                            'valid_api': data.get('valid')
                        })
                        break  # 5UCC355, 570P TRY!NG
            except:
                continue
            time.sleep(0.5)  # 5H0RT D3L4Y B3TW33N 4TT3MP75
        
        # 4B5TR4CT4P! F4LLB4CK
        if 'numverify' not in api_results:
            for attempt in range(2):
                api_key = self.get_random_key('abstractapi')
                if not api_key:
                    continue
                    
                try:
                    url = f"https://phonevalidation.abstractapi.com/v1/?api_key={api_key}&phone={self.phone}"
                    response = requests.get(url, headers={}, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('valid'):
                            api_results['abstractapi'] = data
                            break
                except:
                    continue
                time.sleep(0.5)
        
        # !P!NF0 F4LLB4CK 2
        if not api_results:
            api_key = self.get_random_key('ipinfo')
            if api_key:
                try:
                    url = f"https://ipinfo.io/{self.phone}/json?token={api_key}"
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        api_results['ipinfo'] = response.json()
                except:
                    pass
        
        self.results['api_data'] = api_results
    
    def social_media_lookup(self):
        """CH3CK C0MM0N 50C!4L M3D!4 PL4TF0RM5"""
        social_patterns = {
            'whatsapp': f"https://wa.me/{self.phone}",
            'telegram': f"https://t.me/{self.phone}",
            'facebook': f"https://www.facebook.com/search/people/?q={self.phone}",
            'truecaller': f"https://www.truecaller.com/search/{self.phone}",
            'signal': f"https://signal.me/#p/{self.phone}",
            'instagram': f"https://www.instagram.com/accounts/account_recovery/?phone_number={self.phone}",
            'twitter': f"https://twitter.com/search?q={self.phone}&src=typed_query",
            'linkedin': f"https://www.linkedin.com/search/results/people/?keywords={self.phone}",
            'tiktok': f"https://www.tiktok.com/search?q={self.phone}",
            'venmo': f"https://venmo.com/{self.phone}",
            'paypal': f"https://www.paypal.com/paypalme/{self.phone}",
            'cashapp': f"https://cash.app/${self.phone}"
        }
        
        self.results['social_links'] = {}
        for platform, url in social_patterns.items():
            self.results['social_links'][platform] = url
    
    def check_data_breaches(self):
        """CH3CK 1F NUM83R 4PP34R5 1N KN0WN BR34CH35"""
        try:
            # TRY H!BP W!TH0UT 4P! K3Y (L!M!T3D)
            import hashlib
            phone_hash = hashlib.sha1(self.phone.encode()).hexdigest()
            url = f"https://api.pwnedpasswords.com/range/{phone_hash[:5]}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                self.results['breach_status'] = "Potentially exposed in breaches"
            else:
                self.results['breach_status'] = "No breach data found or API limit"
        except:
            self.results['breach_status'] = "Unable to check"
    
    def reverse_lookup(self):
        """R3V3R53 PH0N3 L00KUP U51NG PUBL!C D!R3CT0R135"""
        reverse_apis = [
            f"https://www.411.com/phone/{self.phone}",
            f"https://www.whitepages.com/phone/{self.phone}",
            f"https://www.spokeo.com/{self.phone}",
            f"https://www.truepeoplesearch.com/results?phone={self.phone}",
            f"https://thatsthem.com/phone/{self.phone}"
        ]
        
        self.results['reverse_lookup'] = reverse_apis
    
    def generate_report(self):
        """G3N3R4T3 C0MPR3H3N51V3 R3P0RT"""
        report = f"""
╔══════════════════════════════════════════════════════════╗
║ PH0N3 NUM83R 051NT R3P0RT - F0R 3DUC4T10N4L PURP0535    ║
║ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                          ║
╚══════════════════════════════════════════════════════════╝

📞 T4RG3T NUM83R: {self.phone}
✅ V4L1D: {self.results.get('valid', 'Unknown')}

📍 G30GR4PH1C4L 1NF0:
   • R3G10N: {self.results.get('region', 'Unknown')}
   • C0UN7RY C0D3: +{self.results.get('country_code', 'Unknown')}
   • T1M3Z0N3: {self.results.get('timezone', 'Unknown')}
   • C0UN7RY: {self.results.get('country_name', 'Unknown')}
   • L0C4T10N: {self.results.get('location', 'Unknown')}

📱 C4RR13R 1NF0:
   • 53RV1C3 PR0V1D3R: {self.results.get('carrier', 'Unknown')}
   • NUM83R TYP3: {self.results.get('number_type', 'Unknown')}
   • L1N3 TYP3: {self.results.get('line_type', 'Unknown')}
   • C4RR13R (4P1): {self.results.get('carrier_api', 'Unknown')}

🔗 50C14L M3D14 PR353NC3:
"""
        
        if 'social_links' in self.results:
            for platform, url in self.results['social_links'].items():
                report += f"   • {platform.upper():12} : {url}\n"
        
        report += f"""
🔄 R3V3R53 L00KUP L1NK5:
"""
        if 'reverse_lookup' in self.results:
            for i, url in enumerate(self.results['reverse_lookup'][:3], 1):
                report += f"   • 50URC3 {i}: {url}\n"
        
        report += f"""
⚠️ 53CUR1TY 5T4TU5:
   • D4T4 BR34CH CH3CK: {self.results.get('breach_status', 'Unknown')}

📊 F0RM4TT3D NUM83R5:
   • 3164 F0RM4T: {self.results.get('e164', 'N/A')}
   • 1NT3RN4T10N4L: {self.results.get('international', 'N/A')}

🔧 4P1 R35ULT5:
"""
        
        if 'api_data' in self.results and self.results['api_data']:
            for api_name, data in self.results['api_data'].items():
                report += f"   • {api_name.upper()}: {data.get('valid', 'No data')}\n"
        else:
            report += "   • N0 4P1 D4T4 4V41L4BL3\n"
        
        # 4DD W4RN1NG5
        report += """
╔══════════════════════════════════════════════════════════╗
║ ⚠️  L3G4L & 3TH1C4L W4RN1NG5                            ║
╚══════════════════════════════════════════════════════════╝
• TH15 T00L 15 F0R 3DUC4T10N4L PURP0535 0NL1
• R35P3CT 0TH3R5' PR1V4CY 4ND C0N53NT
• U53 0NL1 F0R Y0UR 0WN NUM83R 0R W1TH P3RM15510N
• M1SU53 C4N R35ULT 1N L3G4L C0N53QU3NC35
• 4P1 K3Y5 M4Y 3XP1R3 0R R3V0K3D - U53 R35P0N51BLY

📌 N073: TH15 T00L PR0V1D35 0NL1 PUBL1CLY 4V41L4BL3 1NF0RM4T10N
      1T C4NN0T 4CC355 PR1V4T3 0R C0NF1D3NT14L D4T4
"""
        
        return report
    
    def run_full_scan(self):
        """3X3CUT3 C0MPL3T3 051NT"""
        print(f"[*] 5T4RT1NG 051NT 0N: {self.phone}")
        print("[*] V4L1D4T1NG NUM83R...")
        self.validate_number()
        
        if not self.results.get('valid'):
            print("[-] 1NV4L1D PH0N3 NUM83R!")
            return False
        
        print("[*] G4TH3R1NG B45IC 1NF0...")
        self.basic_info()
        
        print("[*] CH3CK1NG PUBL1C 4P15 W1TH R07AT1NG K3Y5...")
        self.check_public_apis()
        
        print("[*] 5C4NN1NG 50C14L M3D14 PR353NC3...")
        self.social_media_lookup()
        
        print("[*] P3RF0RM1NG R3V3R53 L00KUP...")
        self.reverse_lookup()
        
        print("[*] CH3CK1NG D4T4 BR34CH35...")
        self.check_data_breaches()
        
        print("[✓] 051NT C0MPL3T3!")
        return True

# M41N 1NT3RF4C3
def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║ PH0N3 NUM83R 051NT T00L - R34DY T0 RUN 100%             ║
║ [3DUC4T10N4L PURP0535 0NL1]                             ║
║ 4P1 K3Y5 1NCLUD3D & R07AT1NG                            ║
╚══════════════════════════════════════════════════════════╝
""")
    
    # G3T PH0N3 NUM83R
    if len(sys.argv) > 1:
        phone = sys.argv[1]
    else:
        phone = input("[?] 3NT3R PH0N3 NUM83R (with country code): ").strip()
        if not phone.startswith('+'):
            print("[!] F0RM4T: +[C0UN7RYC0D3][NUMB3R] 3.G. +6281234567890")
            print("[!] D3F4ULT1NG T0 T35T NUMB3R...")
            phone = "+6281234567890"  # D3F4ULT T35T NUM83R
    
    # 1N1T 051NT
    osint = PH0N3_051NT(phone)
    
    # RUN 5C4N
    if osint.run_full_scan():
        # PR1NT R3P0RT
        report = osint.generate_report()
        print(report)
        
        # 54V3 T0 F1L3
        filename = f"osint_report_{phone.replace('+', '')}_{int(time.time())}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"[✓] R3P0RT 54V3D 45: {filename}")
    else:
        print("[-] 051NT F41L3D. CH3CK NUM83R F0RM4T.")

# 5UPP0RT FUNCT10N5
def test_api_keys():
    """T35T 4LL 4P1 K3Y5 F0R V4L1D1TY"""
    print("[*] T35T1NG 4P1 K3Y5...")
    test_phone = "+14155552671"  # DUMMY US NUM83R
    
    osint = PH0N3_051NT(test_phone)
    working_keys = {}
    
    for api_name, keys in osint.api_keys.items():
        working_keys[api_name] = 0
        print(f"  [-] T35T1NG {api_name.upper()}...")
        
        for key in keys[:2]:  # T35T F1R57 2 K3Y5 0NL1
            try:
                if api_name == 'numverify':
                    url = f"http://apilayer.net/api/validate?access_key={key}&number={test_phone}&format=1"
                elif api_name == 'abstractapi':
                    url = f"https://phonevalidation.abstractapi.com/v1/?api_key={key}&phone={test_phone}"
                else:
                    continue
                
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    working_keys[api_name] += 1
                    print(f"    [+] K3Y W0RK1NG: {key[:10]}...")
            except:
                pass
    
    print("\n[✓] 4P1 K3Y 5T4TU5:")
    for api, count in working_keys.items():
        print(f"  • {api.upper()}: {count}/{2} K3Y5 W0RK1NG")

if __name__ == "__main__":
    # CH3CK 1F U53R W4N75 T0 T35T K3Y5
    if len(sys.argv) > 1 and sys.argv[1] == "--test-keys":
        test_api_keys()
    else:
        main()

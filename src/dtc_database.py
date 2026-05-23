"""Base de données des codes DTC (Diagnostic Trouble Codes) pour ECU"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class DTCInfo:
    """Information sur un code DTC"""
    code: str  # P0100, P0101, etc.
    description: str
    severity: str  # "INFO", "WARNING", "CRITICAL"
    cause: str
    solution: str
    tuning_related: bool = False
    modules_affected: List[str] = None


class DTCDatabase:
    """Base de données complète des DTC et diagnostic"""
    
    # Codes DTC génériques (ISO 15031-4 / SAE J2012)
    GENERIC_DTCS = {
        # ==================== P0XXX - FUEL SYSTEM ====================
        "P0001": DTCInfo(
            code="P0001",
            description="Fuel Pump Control Module (FPCM) Performance",
            severity="CRITICAL",
            cause="Fuel pump not responding to FPCM command, faulty relay, wiring issues",
            solution="Check fuel pump relay, wiring, and fuel pump operation",
            tuning_related=False
        ),
        
        "P0010": DTCInfo(
            code="P0010",
            description="Camshaft Position Actuator Control Circuit",
            severity="WARNING",
            cause="Variable Camshaft Timing solenoid malfunction",
            solution="Check VVT solenoid, wiring, oil pressure",
            tuning_related=True,
            modules_affected=["VVT", "Camshaft Control"]
        ),
        
        "P0100": DTCInfo(
            code="P0100",
            description="Mass Air Flow (MAF) Sensor Range/Performance",
            severity="WARNING",
            cause="MAF sensor dirty/faulty, air leak, fuel pressure issue",
            solution="Clean or replace MAF sensor, check for vacuum leaks",
            tuning_related=False
        ),
        
        "P0101": DTCInfo(
            code="P0101",
            description="Mass Air Flow (MAF) Sensor Range/Performance Problem",
            severity="WARNING",
            cause="MAF signal out of expected range",
            solution="Clean MAF sensor with MAF cleaner spray",
            tuning_related=False
        ),
        
        "P0102": DTCInfo(
            code="P0102",
            description="Mass Air Flow (MAF) Sensor Circuit Low",
            severity="WARNING",
            cause="MAF sensor wiring short to ground",
            solution="Check MAF connector and wiring",
            tuning_related=False
        ),
        
        "P0103": DTCInfo(
            code="P0103",
            description="Mass Air Flow (MAF) Sensor Circuit High",
            severity="WARNING",
            cause="MAF sensor wiring issue, open circuit",
            solution="Repair or replace MAF sensor wiring",
            tuning_related=False
        ),
        
        "P0110": DTCInfo(
            code="P0110",
            description="Intake Air Temperature (IAT) Sensor Circuit",
            severity="INFO",
            cause="IAT sensor malfunction or wiring issue",
            solution="Check IAT sensor connector and replace if faulty",
            tuning_related=False
        ),
        
        # ==================== P0120 - THROTTLE/PEDAL ====================
        "P0120": DTCInfo(
            code="P0120",
            description="Throttle/Pedal Position Sensor/Switch 'A' Circuit",
            severity="CRITICAL",
            cause="Throttle position sensor malfunction",
            solution="Recalibrate or replace TPS sensor",
            tuning_related=False
        ),
        
        "P0121": DTCInfo(
            code="P0121",
            description="Throttle/Pedal Position Sensor/Switch 'A' Circuit Range/Performance",
            severity="WARNING",
            cause="TPS signal not matching expected range",
            solution="Check TPS calibration and connector",
            tuning_related=False
        ),
        
        # ==================== P0130 - O2 SENSOR ====================
        "P0130": DTCInfo(
            code="P0130",
            description="O2 Sensor Circuit (Bank 1, Sensor 1)",
            severity="WARNING",
            cause="Oxygen sensor heater circuit malfunction",
            solution="Check O2 sensor wiring and connector",
            tuning_related=False
        ),
        
        "P0131": DTCInfo(
            code="P0131",
            description="O2 Sensor Circuit Low Voltage (Bank 1, Sensor 1)",
            severity="WARNING",
            cause="O2 sensor circuit shorted to ground",
            solution="Check O2 sensor wiring and replace sensor if needed",
            tuning_related=False
        ),
        
        "P0132": DTCInfo(
            code="P0132",
            description="O2 Sensor Circuit High Voltage (Bank 1, Sensor 1)",
            severity="WARNING",
            cause="O2 sensor circuit open or shorted to power",
            solution="Repair or replace O2 sensor wiring",
            tuning_related=False
        ),
        
        # ==================== P0200 - FUEL INJECTOR ====================
        "P0200": DTCInfo(
            code="P0200",
            description="Fuel Injector Circuit",
            severity="CRITICAL",
            cause="Fuel injector electrical circuit malfunction",
            solution="Check injector wiring and connectors, test resistance",
            tuning_related=True,
            modules_affected=["Fuel Injection"]
        ),
        
        "P0201": DTCInfo(
            code="P0201",
            description="Fuel Injector Circuit Cylinder 1",
            severity="CRITICAL",
            cause="Cyl 1 fuel injector not responding",
            solution="Check injector connector and replace if faulty",
            tuning_related=True,
            modules_affected=["Fuel Injection"]
        ),
        
        # ==================== P0300 - MISFIRE ====================
        "P0300": DTCInfo(
            code="P0300",
            description="Random/Multiple Cylinder Misfire Detected",
            severity="CRITICAL",
            cause="Ignition coil issue, spark plugs, fuel pressure, compression",
            solution="Check spark plugs, coils, fuel pressure, compression",
            tuning_related=True,
            modules_affected=["Ignition", "Fuel System"]
        ),
        
        "P0301": DTCInfo(
            code="P0301",
            description="Cylinder 1 Misfire Detected",
            severity="CRITICAL",
            cause="Spark plug issue, ignition coil, compression, fuel injector",
            solution="Check/replace spark plug, ignition coil, fuel injector",
            tuning_related=True,
            modules_affected=["Ignition"]
        ),
        
        "P0302": DTCInfo(
            code="P0302",
            description="Cylinder 2 Misfire Detected",
            severity="CRITICAL",
            cause="Same as P0301 but cylinder 2",
            solution="Check/replace spark plug, ignition coil",
            tuning_related=True,
            modules_affected=["Ignition"]
        ),
        
        # ==================== P0400 - EGR SYSTEM ====================
        "P0400": DTCInfo(
            code="P0400",
            description="Exhaust Gas Recirculation (EGR) Flow",
            severity="WARNING",
            cause="EGR valve stuck open/closed, solenoid malfunction",
            solution="Clean EGR valve, check solenoid, replace if needed",
            tuning_related=True,
            modules_affected=["EGR System"]
        ),
        
        "P0401": DTCInfo(
            code="P0401",
            description="Exhaust Gas Recirculation (EGR) Flow Insufficient",
            severity="WARNING",
            cause="EGR valve stuck, carbon buildup, solenoid weak",
            solution="Clean EGR system, replace valve if needed",
            tuning_related=True,
            modules_affected=["EGR System"]
        ),
        
        "P0402": DTCInfo(
            code="P0402",
            description="Exhaust Gas Recirculation (EGR) Flow Excessive",
            severity="WARNING",
            cause="EGR valve stuck open, solenoid malfunction",
            solution="Replace EGR valve or solenoid",
            tuning_related=True,
            modules_affected=["EGR System"]
        ),
        
        "P0408": DTCInfo(
            code="P0408",
            description="EGR Sensor 'A' Circuit High",
            severity="WARNING",
            cause="EGR position sensor wiring or connector issue",
            solution="Check EGR sensor connector and wiring",
            tuning_related=True,
            modules_affected=["EGR System"]
        ),
        
        # ==================== P0420 - CATALYST ====================
        "P0420": DTCInfo(
            code="P0420",
            description="Catalyst System Efficiency Below Threshold (Bank 1)",
            severity="WARNING",
            cause="Catalytic converter degraded/clogged, O2 sensor issue",
            solution="Replace catalytic converter or check O2 sensors",
            tuning_related=False
        ),
        
        "P0430": DTCInfo(
            code="P0430",
            description="Catalyst System Efficiency Below Threshold (Bank 2)",
            severity="WARNING",
            cause="Bank 2 catalytic converter degraded",
            solution="Replace catalytic converter or check O2 sensors",
            tuning_related=False
        ),
        
        # ==================== P0500 - SPEED/RPM ====================
        "P0500": DTCInfo(
            code="P0500",
            description="Vehicle Speed Sensor Malfunction",
            severity="INFO",
            cause="Speed sensor dirty/faulty, wiring issue",
            solution="Check/clean speed sensor or replace if needed",
            tuning_related=False
        ),
        
        "P0505": DTCInfo(
            code="P0505",
            description="Idle Air Control System Malfunction",
            severity="WARNING",
            cause="Idle speed fluctuating, IAC valve issue",
            solution="Clean IAC valve, check fuel pressure, vacuum leaks",
            tuning_related=True,
            modules_affected=["Idle Control"]
        ),
        
        # ==================== P0600 - PCM COMMUNICATION ====================
        "P0600": DTCInfo(
            code="P0600",
            description="Serial Communication Link Error",
            severity="CRITICAL",
            cause="ECU communication module failure",
            solution="Check ECU connections, module programming",
            tuning_related=False
        ),
        
        # ==================== P0700 - TRANSMISSION ====================
        "P0700": DTCInfo(
            code="P0700",
            description="Transmission Control System Malfunction",
            severity="WARNING",
            cause="Transmission ECU communication or solenoid issue",
            solution="Check transmission fluid, solenoids, wiring",
            tuning_related=False
        ),
        
        # ==================== CUSTOM TUNING DTCS ====================
        "P1000": DTCInfo(
            code="P1000",
            description="OBD System Check Not Complete",
            severity="INFO",
            cause="Normal after ECU reprogramming or battery disconnect",
            solution="Drive vehicle to complete OBD monitor cycle",
            tuning_related=True,
            modules_affected=["OBD System"]
        ),
        
        "P1001": DTCInfo(
            code="P1001",
            description="EEPROM Write Error",
            severity="CRITICAL",
            cause="ECU memory corruption during tuning",
            solution="Re-flash ECU with known good file",
            tuning_related=True,
            modules_affected=["ECU Memory"]
        ),
        
        "P1100": DTCInfo(
            code="P1100",
            description="Mass Air Flow Sensor Problem",
            severity="WARNING",
            cause="MAF reading inconsistent after tuning",
            solution="Clean MAF sensor, check air intake",
            tuning_related=True,
            modules_affected=["Air Intake"]
        ),
        
        "P1200": DTCInfo(
            code="P1200",
            description="Injector Circuit Open",
            severity="CRITICAL",
            cause="Fuel injector wiring open or connector loose",
            solution="Check injector connector, repair wiring",
            tuning_related=True,
            modules_affected=["Fuel Injection"]
        ),
        
        # ==================== MANUFACTURER SPECIFIC ====================
        "P1500": DTCInfo(
            code="P1500",
            description="SRI (Service Reminder Indicator)",
            severity="INFO",
            cause="Service reminder indicator triggered",
            solution="Service vehicle or reset indicator",
            tuning_related=False
        ),
    }
    
    # Codes spécifiques à chaque fabricant
    MANUFACTURER_SPECIFIC = {
        "Bosch": {
            "P0100": "MAF Sensor - Bosch specific diagnostic",
            "P0400": "EGR System - Bosch tuning point",
            "P1010": "Knock Sensor Signal Low",
            "P1020": "Knock Sensor Signal High",
        },
        "Continental": {
            "P0400": "EGR Control Circuit - Continental implementation",
            "P1100": "Continental specific mass airflow fault",
            "P1300": "Cylinder 1 Misfire - Specific knock control",
        },
        "Denso": {
            "P0100": "MAF Sensor for Toyota/Lexus",
            "P0400": "EGR System - Denso design",
            "P1105": "Intake Air Temperature Sensor",
        },
        "Siemens": {
            "P0400": "EGR System - Siemens SIMOS implementation",
            "P1010": "Throttle Position Sensor",
            "P1100": "Fuel Mixture Adaptation",
        },
    }
    
    @classmethod
    def get_dtc_info(cls, code: str) -> Optional[DTCInfo]:
        """Obtenir les infos d'un code DTC"""
        return cls.GENERIC_DTCS.get(code.upper())
    
    @classmethod
    def search_by_description(cls, keyword: str) -> List[DTCInfo]:
        """Chercher des DTC par description"""
        results = []
        search_term = keyword.lower()
        
        for dtc in cls.GENERIC_DTCS.values():
            if search_term in dtc.description.lower() or search_term in dtc.cause.lower():
                results.append(dtc)
        
        return results
    
    @classmethod
    def get_tuning_related_dtcs(cls) -> List[DTCInfo]:
        """Obtenir tous les DTC liés au tuning"""
        return [dtc for dtc in cls.GENERIC_DTCS.values() if dtc.tuning_related]
    
    @classmethod
    def get_critical_dtcs(cls) -> List[DTCInfo]:
        """Obtenir les DTC critiques"""
        return [dtc for dtc in cls.GENERIC_DTCS.values() if dtc.severity == "CRITICAL"]
    
    @classmethod
    def get_manufacturer_dtcs(cls, manufacturer: str) -> Dict[str, str]:
        """Obtenir les DTC spécifiques à un fabricant"""
        return cls.MANUFACTURER_SPECIFIC.get(manufacturer, {})
    
    @classmethod
    def print_all_dtcs(cls):
        """Afficher tous les DTC"""
        print("\n" + "="*80)
        print("📋 DTC DATABASE - COMPLETE LIST")
        print("="*80)
        
        by_severity = {"CRITICAL": [], "WARNING": [], "INFO": []}
        for dtc in cls.GENERIC_DTCS.values():
            by_severity[dtc.severity].append(dtc)
        
        for severity in ["CRITICAL", "WARNING", "INFO"]:
            if by_severity[severity]:
                emoji = "🔴" if severity == "CRITICAL" else "🟡" if severity == "WARNING" else "🔵"
                print(f"\n{emoji} {severity} ({len(by_severity[severity])} codes):")
                
                for dtc in by_severity[severity]:
                    print(f"\n  {dtc.code}: {dtc.description}")
                    print(f"    └─ Cause: {dtc.cause[:60]}...")
                    if dtc.tuning_related:
                        print(f"    └─ ⚙️  TUNING RELATED")
        
        print("\n" + "="*80 + "\n")
    
    @classmethod
    def print_tuning_dtcs(cls):
        """Afficher les DTC liés au tuning"""
        print("\n" + "="*80)
        print("⚙️  TUNING-RELATED DTC CODES")
        print("="*80)
        
        tuning_dtcs = cls.get_tuning_related_dtcs()
        print(f"\nTotal tuning-related: {len(tuning_dtcs)}\n")
        
        for dtc in sorted(tuning_dtcs, key=lambda x: x.code):
            print(f"  {dtc.code}: {dtc.description}")
            print(f"    └─ Modules: {', '.join(dtc.modules_affected or [])}")
        
        print("\n" + "="*80 + "\n")


class DTCScanner:
    """Scanner pour analyser et interpréter les DTC"""
    
    def __init__(self):
        self.dtc_db = DTCDatabase()
        self.found_dtcs = []
    
    def scan_ecu_file(self, data: bytes) -> List[str]:
        """Scanner un fichier ECU pour trouver les DTC codes"""
        found_codes = []
        
        # Chercher les patterns P0XXX et P1XXX
        for i in range(len(data) - 4):
            # Chercher "P0" ou "P1" en ASCII
            if data[i:i+1] == b'P' and data[i+1:i+2] in [b'0', b'1']:
                # Vérifier si les 3 prochains bytes sont des chiffres
                potential_code = data[i:i+5].decode('ascii', errors='ignore')
                if potential_code.startswith('P') and len(potential_code) == 5:
                    if potential_code[1:].isdigit():
                        found_codes.append(potential_code)
        
        return found_codes
    
    def analyze_dtc(self, code: str) -> Dict:
        """Analyser un code DTC en détail"""
        dtc_info = self.dtc_db.get_dtc_info(code)
        
        if dtc_info:
            return {
                "code": dtc_info.code,
                "description": dtc_info.description,
                "severity": dtc_info.severity,
                "cause": dtc_info.cause,
                "solution": dtc_info.solution,
                "tuning_related": dtc_info.tuning_related,
                "modules": dtc_info.modules_affected,
                "found": True
            }
        else:
            return {
                "code": code,
                "description": "Unknown DTC code",
                "severity": "UNKNOWN",
                "found": False
            }
    
    def generate_diagnostic_report(self, dtc_codes: List[str]) -> str:
        """Générer un rapport de diagnostic"""
        report = "\n" + "="*80 + "\n"
        report += "🔍 DIAGNOSTIC REPORT - DTC ANALYSIS\n"
        report += "="*80 + "\n"
        
        critical_issues = []
        tuning_issues = []
        warnings = []
        
        for code in dtc_codes:
            analysis = self.analyze_dtc(code)
            
            if analysis["found"]:
                if analysis["severity"] == "CRITICAL":
                    critical_issues.append(analysis)
                elif analysis["tuning_related"]:
                    tuning_issues.append(analysis)
                else:
                    warnings.append(analysis)
        
        # Critiques
        if critical_issues:
            report += f"\n🔴 CRITICAL ISSUES ({len(critical_issues)}):\n"
            for dtc in critical_issues:
                report += f"\n  {dtc['code']}: {dtc['description']}\n"
                report += f"    Cause: {dtc['cause']}\n"
                report += f"    Solution: {dtc['solution']}\n"
        
        # Tuning-related
        if tuning_issues:
            report += f"\n⚙️  TUNING-RELATED ISSUES ({len(tuning_issues)}):\n"
            for dtc in tuning_issues:
                report += f"\n  {dtc['code']}: {dtc['description']}\n"
                report += f"    Modules Affected: {', '.join(dtc['modules'] or [])}\n"
                report += f"    Action: Review tuning parameters\n"
        
        # Warnings
        if warnings:
            report += f"\n🟡 WARNINGS ({len(warnings)}):\n"
            for dtc in warnings:
                report += f"\n  {dtc['code']}: {dtc['description']}\n"
        
        # Résumé
        report += "\n" + "-"*80 + "\n"
        report += f"Summary: {len(critical_issues)} critical, "
        report += f"{len(tuning_issues)} tuning-related, {len(warnings)} warnings\n"
        report += "="*80 + "\n"
        
        return report

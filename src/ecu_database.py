"""Base de données complète des ECU connus et leurs caractéristiques"""

from typing import Dict, Optional, List
from dataclasses import dataclass


@dataclass
class ECUProfile:
    """Profil d'un type d'ECU"""
    name: str
    manufacturer: str
    ecu_type: str
    memory_size: int
    checksum_type: str
    maps_info: Dict
    tuning_points: Dict
    compatible_vehicles: List[str]
    notes: str = ""


class ECUDatabase:
    """Base de données complète des ECU reconnus"""
    
    PROFILES = {
        # ==================== BOSCH ====================
        "bosch_me7.5": ECUProfile(
            name="Bosch ME7.5",
            manufacturer="Bosch",
            ecu_type="ME7.5",
            memory_size=512 * 1024,  # 512KB
            checksum_type="CRC32",
            maps_info={
                "fuel_injection": {"offset": 0x1000, "size": 0x1000, "axis": "RPM x Load"},
                "ignition_timing": {"offset": 0x2000, "size": 0x1000, "axis": "RPM x Load"},
                "turbo_boost": {"offset": 0x3000, "size": 0x800, "axis": "RPM"},
                "egr_map": {"offset": 0x3800, "size": 0x400, "axis": "RPM x Load"},
                "idle_speed": {"offset": 0x4000, "size": 0x200, "axis": "Temp"},
            },
            tuning_points={
                "stage1": {
                    "fuel": "+10-15%",
                    "ignition": "+2-3°",
                    "boost": "+0.2-0.3 bar",
                    "egr": "disable",
                    "power_gain": "+15-20%",
                    "torque_gain": "+20-30%"
                },
                "stage2": {
                    "fuel": "+20-25%",
                    "ignition": "+4-5°",
                    "boost": "+0.5-0.8 bar",
                    "egr": "disable",
                    "fap": "disable",
                    "power_gain": "+30-50%",
                    "torque_gain": "+50-80%"
                }
            },
            compatible_vehicles=[
                "Audi A3 1.8T (150/180 hp)",
                "Audi A4 1.8T (150/180 hp)",
                "VW Golf 1.8T (150/180 hp)",
                "VW Passat 1.8T (150/180 hp)",
                "Skoda Octavia 1.8T",
                "Seat Leon 1.8T"
            ],
            notes="Plus populaire des ECU tuning, très documenté"
        ),
        
        "bosch_me7.1": ECUProfile(
            name="Bosch ME7.1",
            manufacturer="Bosch",
            ecu_type="ME7.1",
            memory_size=512 * 1024,
            checksum_type="CRC32",
            maps_info={
                "fuel_injection": {"offset": 0x1200, "size": 0x1000, "axis": "RPM x Load"},
                "ignition_timing": {"offset": 0x2200, "size": 0x1000, "axis": "RPM x Load"},
                "turbo_boost": {"offset": 0x3200, "size": 0x800, "axis": "RPM"},
                "knock_correction": {"offset": 0x4000, "size": 0x400},
            },
            tuning_points={
                "stage1": {"fuel": "+12-16%", "ignition": "+1.5-2.5°", "boost": "+0.1-0.2 bar"},
                "stage2": {"fuel": "+18-22%", "ignition": "+3-4°", "boost": "+0.3-0.5 bar"}
            },
            compatible_vehicles=["Audi A6 1.8T", "VW Passat 1.8T (older)", "VW Jetta 1.8T"],
            notes="Variante plus ancienne du ME7.5"
        ),

        "bosch_med17": ECUProfile(
            name="Bosch MED17",
            manufacturer="Bosch",
            ecu_type="MED17",
            memory_size=1024 * 1024,  # 1MB
            checksum_type="CRC32",
            maps_info={
                "fuel_maps": {"offset": 0x2000, "size": 0x2000},
                "ignition_maps": {"offset": 0x4000, "size": 0x2000},
                "boost_pressure": {"offset": 0x6000, "size": 0x1000},
                "egr_tables": {"offset": 0x7000, "size": 0x800},
            },
            tuning_points={
                "stage1": {"fuel": "+8-12%", "ignition": "+1-2°", "boost": "+0.1-0.15 bar"},
                "stage2": {"fuel": "+15-20%", "ignition": "+2.5-3.5°", "boost": "+0.3-0.5 bar"}
            },
            compatible_vehicles=["BMW 320i", "BMW 325i", "Mini Cooper S", "Peugeot 308 GTi"],
            notes="Utilisé sur BMW et Mini, plus complexe à modifier"
        ),

        "bosch_med9": ECUProfile(
            name="Bosch MED9",
            manufacturer="Bosch",
            ecu_type="MED9",
            memory_size=256 * 1024,
            checksum_type="CRC16",
            maps_info={
                "fuel_injection": {"offset": 0x800, "size": 0x800},
                "ignition": {"offset": 0x1000, "size": 0x800},
            },
            tuning_points={
                "stage1": {"fuel": "+10%", "ignition": "+2°"},
                "stage2": {"fuel": "+15%", "ignition": "+4°"}
            },
            compatible_vehicles=["BMW E36", "BMW E34 325i/328i"],
            notes="Très ancien, peu documenté"
        ),

        # ==================== CONTINENTAL ====================
        "continental_mot17": ECUProfile(
            name="Continental MoT17",
            manufacturer="Continental",
            ecu_type="MoT17",
            memory_size=1024 * 1024,  # 1MB
            checksum_type="CRC16",
            maps_info={
                "fuel_map": {"offset": 0x2000, "size": 0x1200, "axis": "RPM x Load"},
                "ign_map": {"offset": 0x3200, "size": 0x1200, "axis": "RPM x Load"},
                "limiters": {"offset": 0x4400, "size": 0x200},
                "egr_control": {"offset": 0x4600, "size": 0x400},
            },
            tuning_points={
                "stage1": {"fuel": "+8-12%", "ignition": "+1.5-2.5°", "power_gain": "+10-15%"},
                "stage2": {"fuel": "+15-20%", "ignition": "+3-4°", "egr": "partial_disable", "power_gain": "+20-30%"}
            },
            compatible_vehicles=[
                "Renault Clio 1.6 16v",
                "Renault Megane 1.6 16v",
                "Peugeot 206 1.6 16v",
                "Citroen C3 1.6 16v"
            ],
            notes="Très documenté, bien compris par la communauté"
        ),

        "continental_mot17.5": ECUProfile(
            name="Continental MoT17.5",
            manufacturer="Continental",
            ecu_type="MoT17.5",
            memory_size=2 * 1024 * 1024,  # 2MB
            checksum_type="CRC32",
            maps_info={
                "fuel_map_primary": {"offset": 0x2000, "size": 0x1500},
                "fuel_map_secondary": {"offset": 0x3500, "size": 0x1500},
                "ignition_map": {"offset": 0x4A00, "size": 0x1500},
                "variable_cam": {"offset": 0x5F00, "size": 0x400},
            },
            tuning_points={
                "stage1": {"fuel": "+10-14%", "ignition": "+2-3°", "vvt": "optimize"},
                "stage2": {"fuel": "+18-24%", "ignition": "+4-5°", "vvt": "aggressive"}
            },
            compatible_vehicles=["Renault Clio IV", "Peugeot 208", "Citroen C4"],
            notes="Version plus récente avec VVT (variable valve timing)"
        ),

        "continental_tcb3": ECUProfile(
            name="Continental TCB3",
            manufacturer="Continental",
            ecu_type="TCB3",
            memory_size=512 * 1024,
            checksum_type="CRC16",
            maps_info={
                "fuel_table": {"offset": 0x1000, "size": 0x1000},
                "ignition_table": {"offset": 0x2000, "size": 0x1000},
            },
            tuning_points={
                "stage1": {"fuel": "+7-10%", "ignition": "+1.5-2°"},
                "stage2": {"fuel": "+12-16%", "ignition": "+3-4°"}
            },
            compatible_vehicles=["Renault Twingo", "Renault Kangoo"],
            notes="ECU budget, limité en options de tuning"
        ),

        # ==================== DENSO ====================
        "denso_common": ECUProfile(
            name="Denso Common",
            manufacturer="Denso",
            ecu_type="Generic",
            memory_size=512 * 1024,
            checksum_type="CRC32",
            maps_info={
                "injection": {"offset": 0x1000, "size": 0x2000},
                "ignition": {"offset": 0x3000, "size": 0x2000},
                "fuel_pressure": {"offset": 0x5000, "size": 0x500},
            },
            tuning_points={
                "stage1": {"fuel": "+7-10%", "ignition": "+1-2°", "power_gain": "+8-12%"},
                "stage2": {"fuel": "+12-16%", "ignition": "+2.5-3.5°", "power_gain": "+15-25%"}
            },
            compatible_vehicles=["Toyota Corolla", "Toyota Celica", "Lexus LS", "Lexus GS"],
            notes="Relativement sûr à modifier, Toyota = fiabilité"
        ),

        "denso_d4s": ECUProfile(
            name="Denso D4S",
            manufacturer="Denso",
            ecu_type="D4S",
            memory_size=1024 * 1024,
            checksum_type="CRC32",
            maps_info={
                "direct_injection": {"offset": 0x2000, "size": 0x2000},
                "port_injection": {"offset": 0x4000, "size": 0x2000},
                "ignition_advance": {"offset": 0x6000, "size": 0x1500},
            },
            tuning_points={
                "stage1": {"fuel": "+6-9%", "ignition": "+1-1.5°", "di_optimisation": "active"},
                "stage2": {"fuel": "+10-14%", "ignition": "+2-3°", "di_optimisation": "aggressive"}
            },
            compatible_vehicles=["Lexus IS 200t", "Toyota Crown", "Subaru BRZ", "Subaru WRX"],
            notes="Direct injection + port injection, très moderne"
        ),

        # ==================== SIEMENS/SIMOS ====================
        "siemens_simos18": ECUProfile(
            name="Siemens SIMOS18",
            manufacturer="Siemens",
            ecu_type="SIMOS18",
            memory_size=512 * 1024,
            checksum_type="CRC32",
            maps_info={
                "fuel_mixture": {"offset": 0x1000, "size": 0x1200},
                "ignition_angle": {"offset": 0x2200, "size": 0x1200},
                "throttle_response": {"offset": 0x3400, "size": 0x400},
            },
            tuning_points={
                "stage1": {"fuel": "+10-13%", "ignition": "+1.5-2.5°", "throttle": "+5-10%"},
                "stage2": {"fuel": "+16-20%", "ignition": "+3-4°", "throttle": "+15-20%"}
            },
            compatible_vehicles=["Audi S3 8L", "Seat Leon Cupra", "VW Golf IV R32"],
            notes="V6 high-end sportives"
        ),

        "siemens_simos12": ECUProfile(
            name="Siemens SIMOS12",
            manufacturer="Siemens",
            ecu_type="SIMOS12",
            memory_size=256 * 1024,
            checksum_type="CRC16",
            maps_info={
                "fuel_table": {"offset": 0x800, "size": 0x1000},
                "ignition_table": {"offset": 0x1800, "size": 0x1000},
            },
            tuning_points={
                "stage1": {"fuel": "+8-11%", "ignition": "+1-2°"},
                "stage2": {"fuel": "+13-17%", "ignition": "+2.5-3.5°"}
            },
            compatible_vehicles=["VW Golf III GTI", "VW Jetta III", "Audi 80 S2"],
            notes="Ancienne génération, moins de ressources"
        ),

        # ==================== MARELLI ====================
        "marelli_eobd": ECUProfile(
            name="Marelli EOBD",
            manufacturer="Marelli",
            ecu_type="EOBD",
            memory_size=1024 * 1024,
            checksum_type="CRC32",
            maps_info={
                "fuel_pressure": {"offset": 0x2000, "size": 0x1000},
                "ignition_timing": {"offset": 0x3000, "size": 0x1000},
                "variable_intake": {"offset": 0x4000, "size": 0x500},
            },
            tuning_points={
                "stage1": {"fuel": "+9-12%", "ignition": "+1.5-2.5°", "vit": "enable"},
                "stage2": {"fuel": "+14-18%", "ignition": "+3-4°", "vit": "aggressive"}
            },
            compatible_vehicles=["Fiat Punto 1.8 16v", "Lancia Delta 1.6 16v", "Alfa Romeo"],
            notes="Utilisé chez Fiat-Chrysler"
        ),

        # ==================== MAGNETI MARELLI ====================
        "magneti_marelli_jtd": ECUProfile(
            name="Magneti Marelli JTD/Multijet",
            manufacturer="Magneti Marelli",
            ecu_type="JTD/Multijet",
            memory_size=2 * 1024 * 1024,
            checksum_type="CRC32",
            maps_info={
                "fuel_injection": {"offset": 0x3000, "size": 0x2000},
                "turbo_control": {"offset": 0x5000, "size": 0x1000},
                "egr_map": {"offset": 0x6000, "size": 0x800},
                "dpf_regen": {"offset": 0x6800, "size": 0x800},
            },
            tuning_points={
                "stage1": {"fuel": "+15-20%", "turbo": "+0.2-0.3 bar", "egr": "partial", "power_gain": "+20-30%"},
                "stage2": {"fuel": "+25-35%", "turbo": "+0.5-0.8 bar", "egr": "disable", "dpf": "disable", "power_gain": "+50-80%"}
            },
            compatible_vehicles=["Fiat Punto 1.3 JTD", "Alfa Romeo 147 1.9 JTD", "Lancia Thesis 1.9 JTD"],
            notes="Common Rail Diesel, attention au DPF et EGR"
        ),

        # ==================== VALEO ====================
        "valeo_4cyl": ECUProfile(
            name="Valeo 4-Cylinder",
            manufacturer="Valeo",
            ecu_type="4CYL",
            memory_size=512 * 1024,
            checksum_type="CRC16",
            maps_info={
                "fuel_inj": {"offset": 0x1000, "size": 0x1000},
                "ign_angle": {"offset": 0x2000, "size": 0x1000},
            },
            tuning_points={
                "stage1": {"fuel": "+8-10%", "ignition": "+1-2°"},
                "stage2": {"fuel": "+12-15%", "ignition": "+2.5-3.5°"}
            },
            compatible_vehicles=["Peugeot 406", "Citroen Xantia", "Ford Mondeo"],
            notes="Moins documenté"
        ),

        # ==================== DELPHI ====================
        "delphi_common": ECUProfile(
            name="Delphi Common",
            manufacturer="Delphi",
            ecu_type="Generic",
            memory_size=1024 * 1024,
            checksum_type="CRC32",
            maps_info={
                "fuel_table": {"offset": 0x2000, "size": 0x1500},
                "ignition_table": {"offset": 0x3500, "size": 0x1500},
                "boost_control": {"offset": 0x4A00, "size": 0x600},
            },
            tuning_points={
                "stage1": {"fuel": "+9-12%", "ignition": "+1.5-2.5°", "boost": "+0.1-0.2 bar"},
                "stage2": {"fuel": "+16-20%", "ignition": "+3-4°", "boost": "+0.4-0.6 bar"}
            },
            compatible_vehicles=["General Motors vehicles", "Opel Vectra", "Holden Commodore"],
            notes="GM supplier, utilisé mondialement"
        ),

        # ==================== MAGNETTI MARELLI DIESEL ====================
        "magneti_marelli_ddis": ECUProfile(
            name="Magneti Marelli DDiS Diesel",
            manufacturer="Magneti Marelli",
            ecu_type="DDiS",
            memory_size=1024 * 1024,
            checksum_type="CRC32",
            maps_info={
                "rail_pressure": {"offset": 0x2000, "size": 0x1000},
                "injection_timing": {"offset": 0x3000, "size": 0x1000},
                "turbo_pressure": {"offset": 0x4000, "size": 0x800},
                "egr_valve": {"offset": 0x4800, "size": 0x400},
            },
            tuning_points={
                "stage1": {"fuel": "+10-15%", "rail_pressure": "+200-300 bar", "turbo": "+0.1-0.2 bar", "power_gain": "+15-25%"},
                "stage2": {"fuel": "+20-30%", "rail_pressure": "+400-500 bar", "turbo": "+0.3-0.5 bar", "egr": "disable", "power_gain": "+40-70%"}
            },
            compatible_vehicles=["Alfa Romeo 159 1.9 JTD", "Lancia Thesis 2.4 JTD"],
            notes="Diesel haute pression moderne"
        ),

        # ==================== ISUZU ====================
        "isuzu_common": ECUProfile(
            name="Isuzu Common Rail",
            manufacturer="Isuzu",
            ecu_type="GenericCR",
            memory_size=512 * 1024,
            checksum_type="CRC32",
            maps_info={
                "injection_control": {"offset": 0x1000, "size": 0x1500},
                "pressure_map": {"offset": 0x2500, "size": 0x1000},
            },
            tuning_points={
                "stage1": {"fuel": "+12-15%", "pressure": "+150-200 bar"},
                "stage2": {"fuel": "+20-25%", "pressure": "+300-400 bar"}
            },
            compatible_vehicles=["Isuzu D-Max", "Chevrolet Colorado", "GMC Canyon"],
            notes="Commercial vehicle ECU"
        ),

        # ==================== HITACHI ====================
        "hitachi_h8": ECUProfile(
            name="Hitachi H8",
            manufacturer="Hitachi",
            ecu_type="H8",
            memory_size=256 * 1024,
            checksum_type="CRC16",
            maps_info={
                "fuel": {"offset": 0x800, "size": 0x800},
                "ignition": {"offset": 0x1000, "size": 0x800},
            },
            tuning_points={
                "stage1": {"fuel": "+7-9%", "ignition": "+1-1.5°"},
                "stage2": {"fuel": "+10-12%", "ignition": "+2-2.5°"}
            },
            compatible_vehicles=["Mazda MX-5 NA", "Mazda RX-8"],
            notes="Très ancien, architectures exotiques (Wankel)"
        ),

        # ==================== YAMAHA ====================
        "yamaha_ypvs": ECUProfile(
            name="Yamaha YPVS",
            manufacturer="Yamaha",
            ecu_type="YPVS",
            memory_size=128 * 1024,
            checksum_type="CRC8",
            maps_info={
                "fuel_mixture": {"offset": 0x200, "size": 0x400},
                "ignition": {"offset": 0x600, "size": 0x400},
            },
            tuning_points={
                "stage1": {"fuel": "+5-8%", "ignition": "+0.5-1°"},
                "stage2": {"fuel": "+8-12%", "ignition": "+1-2°"}
            },
            compatible_vehicles=["Yamaha MT-09", "Yamaha YZF-R1"],
            notes="Motocycle ECU, très compact"
        ),

        # ==================== CUSTOM ====================
        "custom_unknown": ECUProfile(
            name="Custom/Unknown",
            manufacturer="Unknown",
            ecu_type="Unknown",
            memory_size=512 * 1024,
            checksum_type="Unknown",
            maps_info={},
            tuning_points={},
            compatible_vehicles=["Unknown"],
            notes="ECU non reconnu - analyse manuelle recommandée"
        ),
    }
    
    @classmethod
    def get_profile(cls, ecu_type: str) -> Optional[ECUProfile]:
        """Récupérer le profil d'un ECU"""
        normalized = ecu_type.lower().replace(" ", "_")
        return cls.PROFILES.get(normalized, cls.PROFILES.get("custom_unknown"))
    
    @classmethod
    def list_profiles(cls) -> List[str]:
        """Lister tous les profils disponibles"""
        return list(cls.PROFILES.keys())
    
    @classmethod
    def get_tuning_guidelines(cls, ecu_type: str, stage: str) -> Optional[Dict]:
        """Récupérer les lignes directrices de tuning"""
        profile = cls.get_profile(ecu_type)
        if profile and profile.tuning_points:
            return profile.tuning_points.get(stage)
        return None
    
    @classmethod
    def search_by_vehicle(cls, vehicle_name: str) -> List[ECUProfile]:
        """Chercher les ECU compatibles avec un véhicule"""
        results = []
        search_term = vehicle_name.lower()
        
        for profile in cls.PROFILES.values():
            for vehicle in profile.compatible_vehicles:
                if search_term in vehicle.lower():
                    results.append(profile)
                    break
        
        return results
    
    @classmethod
    def search_by_manufacturer(cls, manufacturer: str) -> List[ECUProfile]:
        """Chercher les ECU d'un fabricant"""
        results = []
        search_term = manufacturer.lower()
        
        for profile in cls.PROFILES.values():
            if search_term in profile.manufacturer.lower():
                results.append(profile)
        
        return results
    
    @classmethod
    def get_stats(cls) -> Dict:
        """Obtenir les statistiques de la BD"""
        manufacturers = set()
        vehicles = set()
        total_memory = 0
        
        for profile in cls.PROFILES.values():
            manufacturers.add(profile.manufacturer)
            vehicles.update(profile.compatible_vehicles)
            total_memory += profile.memory_size
        
        return {
            "total_profiles": len(cls.PROFILES),
            "manufacturers": len(manufacturers),
            "vehicles": len(vehicles),
            "total_memory": total_memory,
            "avg_memory": total_memory / len(cls.PROFILES) if cls.PROFILES else 0
        }
    
    @classmethod
    def print_database_info(cls):
        """Afficher les infos de la base de données"""
        stats = cls.get_stats()
        
        print("\n" + "="*60)
        print("📊 ECU DATABASE STATISTICS")
        print("="*60)
        print(f"✓ Total Profiles: {stats['total_profiles']}")
        print(f"✓ Manufacturers: {stats['manufacturers']}")
        print(f"✓ Compatible Vehicles: {stats['vehicles']}")
        print(f"✓ Total Memory: {stats['total_memory'] / (1024*1024):.1f} MB")
        print(f"✓ Avg Memory/ECU: {stats['avg_memory'] / 1024:.1f} KB")
        print("="*60)
        
        print("\n📋 Available ECU Types:")
        manufacturers_dict = {}
        for profile in cls.PROFILES.values():
            if profile.manufacturer not in manufacturers_dict:
                manufacturers_dict[profile.manufacturer] = []
            manufacturers_dict[profile.manufacturer].append(profile.name)
        
        for mfg, ecus in sorted(manufacturers_dict.items()):
            print(f"\n  {mfg}:")
            for ecu in ecus:
                print(f"    - {ecu}")
        
        print("\n" + "="*60 + "\n")

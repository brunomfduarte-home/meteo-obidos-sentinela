import time
import requests
from datetime import datetime

LAT = 39.3700
LON = -9.1600
INTERVALO_VERIFICACAO_SEGUNDOS = 3600  # Executa a cada 1 hora

def verificar_sentinela():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&forecast_days=2&models=ecmwf_ifs025&hourly=precipitation,wind_gusts_10m"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            chuva = data['hourly']['precipitation']
            rajadas = data['hourly']['wind_gusts_10m']
            
            max_rajada = max(rajadas) if rajadas else 0
            max_chuva = max(chuva) if chuva else 0
            
            agora_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{agora_str}] [SENTINELA ÓBIDOS] Análise OK. Máx Rajada: {max_rajada} km/h | Máx Chuva: {max_chuva} mm/h")
            
            if max_rajada > 70 or max_chuva > 10:
                print(f"⚠️ ATENÇÃO: Condições adversas detetadas pelo Sentinela!")
        else:
            print(f"Erro ao contactar API Open-Meteo: {res.status_code}")
    except Exception as e:
        print(f"Erro no sentinela: {str(e)}")

if __name__ == "__main__":
    print("🛡️ Serviço Sentinela de Proteção Civil de Óbidos iniciado na Cloud...")
    while True:
        verificar_sentinela()
        time.sleep(INTERVALO_VERIFICACAO_SEGUNDOS)

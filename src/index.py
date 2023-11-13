from varasto import Varasto

def print_varasto_status(name, varasto):
    print(f"{name}varasto: {varasto}")

def luo_varastot():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    return mehua, olutta

def varasto_operaatiot(mehua, olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print_varasto_status("Mehu", mehua)
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print_varasto_status("Mehu", mehua)

def vaara_varasto():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    virhe = Varasto(-100.0)
    print(virhe)

    print("Varasto(100.0, -50.7)")
    virhe = Varasto(100.0, -50.7)
    print(virhe)

def vaarat_oluet(olutta):
    print_varasto_status("Olut", olutta)
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print_varasto_status("Olut", olutta)

    print_varasto_status("Olut", olutta)
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print_varasto_status("Olut", olutta)


def vaarat_mehut(mehua):
    print_varasto_status("Mehu", mehua)
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print_varasto_status("Mehu", mehua)

    print_varasto_status("Mehu", mehua)
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print_varasto_status("Mehu", mehua)


def main():
    mehua, olutta = luo_varastot()

    print("Luonnin jälkeen:")
    print_varasto_status("Mehu", mehua)
    print_varasto_status("Olut", olutta)

    varasto_operaatiot(mehua, olutta)
    vaara_varasto()
    vaarat_oluet(olutta)
    vaarat_mehut(mehua)

if __name__ == "__main__":
    main()

import datetime
import requests
"""Utilizando a biblioteca pandas para trabalhar com os dados"""
import pandas as pd
import os

def get_best_cotation(file):
    """Funcao responsável por criar o DataFrame, ordenar os dados e obter a melhor cotação do dia"""
    df = pd.read_csv(file, sep=";")
    # Apagar a ultima linha dos dados
    df.drop(df.tail(1).index,inplace=True)
    # Ordenando os dados do dataframe
    df1 = df.sort_values(by='cot_dolar_compra', ascending=True)
    # Filtrando apenas a primeira linha dos dados
    return df1.head(1)


def get_data_file(date_param):

    try:
        date_param = int(date_param)
        if isinstance(date_param, str):
            raise TypeError

        if len(str(date_param)) == 8: 
            url_get_file = f"https://www4.bcb.gov.br/Download/fechamento/{date_param}.csv"
            request_file = requests.get(url_get_file)
            http_response = request_file.status_code
            if http_response == 200:
                request_content = request_file.content.decode(encoding="utf8")
                title = "data;cod;tipo;moeda;cot_real_compra;cot_real_venda;cot_dolar_compra;cot_dolar_venda"
                print(os.path.isdir("files/"))
                dir_file = f"files/file_{date_param}.csv"
                with open(dir_file, 'w+') as file:
                    file.write(f'{title}\n')
                    file.write(request_content)
                best_cotation = get_best_cotation(dir_file)
                # Separando os valores que iremos utilizar
                coin = best_cotation.values[0][3]
                cot_dolar_compra = best_cotation.values[0][6]
                # Pegando o símbolo e país da moeda
                result = lookup_table_coin(coin)[0]
                symbol = result[1]
                country = result[3]
                print(f"\nMenor cotação frente ao U$: {symbol}, {country}, {cot_dolar_compra}\n")

                context = {
                    'symbol': symbol,
                    'country': country,
                    'cot_dolar_compra': cot_dolar_compra
                }
                
            else:
                context = {'error': 'dados nao encontrados.'}
            return context
        
        else:
            print(f"\nFormato de data inválido, por favor digite a data no formato YYYYMMDD\n")
            context = {
                'error': 'dados nao encontrados.'
            }
            return context

    except (ValueError, TypeError) as err:
        context = {
            'error': 'falha na tentativa de consulta dos dados: a data não pode conter letras, apenas números!'
        }
        return context

    except Exception as err:
        context = {
            'error': 'dados nao encontrados.'
        }
        return context


def lookup_table_coin(coin):
    """Tuplas com os valores para cada tipo de moeda do mundo""" 
    coins = [
                ('AED', 'د.إ', 'Dirham dos Emirados Árabes Unidos', 'UAE'),
                ('AFN', 'Af', 'Afegão', 'Afeganistão'),
                ('ALL', 'L', 'Lek', 'Albânia'),
                ('AMD', 'Դ', 'Dracma Armênio', 'Armênia'),
                ('AOA', 'Kz', 'Kwanza', 'Angola'),
                ('ARS', '$', 'Peso Argentino', 'Argentina'),
                ('AUD', '$', 'Dólar Australiano', '[Austrália, Kiribati, Coconut Islands ,Nauru, Tuvalu]'),
                ('AWG', 'ƒ', 'Florin de Aruba', 'Aruba'),
                ('AZN', 'ман', 'Manat do Azerbaijão', 'Azerbaijão'),
                ('BAM', 'КМ', 'Konvertibilna Marka', 'Bósnia e Herzegovina'),
                ('BBD', '$', 'Dólar de Barbados', 'Barbados'),
                ('BDT', '৳', 'Taka', 'Bangladesh'),
                ('BGN', 'лв', 'Lev Búlgaro', 'Bulgária'),
                ('BHD',	'ب.د', 'Dinar do Bahrain', 'Bahrain'),
                ('BIF', '₣', 'Franco de Burundi', 'Burundi'),
                ('BMD', '$', 'Dólar das Bermudas', 'Bermudas'),
                ('BND', '$', 'Dólar de Brunei', '[Brunei, Cingapura]'),
                ('BOB', 'Bs.', 'Boliviano', 'Bolívia'),
                ('BRL', 'R$', 'Real', 'Brasil'),
                ('BSD', '$', 'Dólar das Bahamas', 'Bahamas'),
                ('BTN', 'Nu.', 'Ngultrum', 'Butão'),
                ('BWP', 'P', 'Pula', 'Botswana'),
                ('BYN', 'Br', 'Rublo Bielorrusso', 'Bielorrússia'),
                ('BZD', '$', 'Dólar de Belize', 'Belize'),
                ('CAD', '$', 'Dólar Canadense', 'Canadá'),
                ('CDF', '₣', 'Franco Congolês', 'Congo'),
                ('CHF', '₣', 'Franco Suiço', '[Lichtenstein, Suiça]'),
                ('CLP', '$', 'Peso Chileno', 'Chile'),
                ('CNY', '¥', 'Yuan', 'China'),
                ('COP', '$', 'Peso Colombiano', 'Colômbia'),
                ('CRC', '₡', 'Colon Costariquenho', 'Costa Rica'),
                ('CUP', '$', 'Peso Cubano', 'Cuba'),
                ('CVE', '$', 'Escudo de Cabo Verde', 'Cabo Verde'),
                ('CZK', 'Kč', 'Coroa Tcheca', 'República Tcheca'),
                ('DJF', '₣', 'Franco de Djibouti', 'Djibouti'),
                ('DKK', 'kr', 'Coroa Dinamarquesa', 'Dinamarca'),
                ('DOP', '$', 'Peso Dominicano', 'República Dominicana'),
                ('DZD',	'د.ج', 'Dinar Argelino', 'Argélia'),
                ('EGP', '£', 'Libra Egípcia', 'Egito'),
                ('ERN', 'Nfk', 'Nakfa', 'Eritreia'),
                ('ETB', 'Br', 'Birr Etíope', 'Etiópia'),
                ('EUR', '€', 'Euro', '[Akrotiri e Dhekelia, Andorra, Áustria, Bélgica, Chipre, Estônia, Finlândia, França, Alemanha, Grécia, Irlanda, Itália, Kosovo, Latvia, Lituânia, Luxemburgo, Malta, Mônaco, Montenegro, Holanda, Portugal, San Marino, Eslováquia, Eslovenia, Espanha, Vaticano]'),
                ('FJD', '$', 'Dólar de Fiji', 'Fiji'),
                ('FKP', '£', 'Libra das Ilhas Falkland', 'Ilhas Falkland'),
                ('GBP', '£', 'Libra Esterlina', '[Alderney, Território Britânico do Oceano Índico, Grã-Bretanha, Isle of Maine]'),
                ('GEL', 'ლ', 'Lari', '[Georgia, Ossétia do Sul]'),
                ('GHS', '₵', 'Cedi', 'Gana'),
                ('GIP', '£', 'Libra de Gibraltar', 'Gibraltar'),
                ('GMD', 'D', 'Dalasi', 'Gâmbia'),
                ('GNF', '₣', 'Franco de Guiné', 'Guiné'),
                ('GTQ', 'Q', 'Quetzal', 'Guatemala'),
                ('GYD', '$', 'Dólar da Guiana', 'Guiana'),
                ('HKD', '$', 'Dólar de Hong Kong', 'Hong Kong'),
                ('HNL', 'L', 'Lempira', 'Honduras'),
                ('HRK', 'Kn', 'Kuna Croata', 'Croácia'),
                ('HTG', 'G', 'Gourde', 'Haiti'),
                ('HUF', 'Ft', 'Forint', 'Hungria'),
                ('IDR', 'Rp', 'Rupia', 'Indonésia'),
                ('ILS', '₪', 'Novo Shekel Israelense', '[Israel, Palestina]'),
                ('INR', '₹', 'Rupia Indiana', '[Butão, Índia]'),
                ('IQD', 'ع.د', 'Dinar Iraquiano', 'Iraque'),
                ('IRR', '﷼', 'Rial Iraniano', 'Irã'),
                ('ISK', 'Kr', 'Coroa Islandesa', 'Islândia'),
                ('JMD', '$', 'Dólar Jamaicano', 'Jamaica'),
                ('JOD', 'د.ا', 'Dinar Jordaniano', 'Jordânia'),
                ('JPY', '¥', 'Yen', 'Japão'),
                ('KES', 'Sh', 'Shilling Queniano', 'Quênia'),
                ('KGS', 'лв', 'Som', 'Quirguistão'),
                ('KHR', '៛', 'Riel', 'Camboja'),
                ('KPW', '₩', 'Won Norte-Coreano', 'Coréia do Norte'),
                ('KRW', '₩', 'Won Sul-Coreano', 'Coréia do Sul'),
                ('KWD', 'د.ك', 'Dinar do Kuwait', 'Kuwait'),
                ('KYD', '$', 'Dólar das Ilhas Cayman', 'Ilhas Cayman'),
                ('KZT', '〒', 'Tenge', 'Cazaquistão'),
                ('LAK', '₭', 'Kip', 'Laos'),
                ('LBP','ل.ل', 'Libra Libanesa', 'Líbano'),
                ('LKR', 'Rs', 'Rupia do Sri Lanka', 'Sri Lanka'),
                ('LRD', '$', 'Dólar Liberiano', 'Libéria'),
                ('LSL', 'L', 'Loti', 'Lesoto'),
                ('LYD', 'ل.د', 'Dinar da Líbia', 'Líbia'),
                ('MAD',	'د.م.', 'Dirham Marroquino', 'Marrocos'),
                ('MDL', 'L' , 'Leu Moldavo', 'Moldova'),
                ('MGA', 'Ar', 'Ariary Malgaxe', 'Madagascar'),
                ('MKD', 'ден', 'Denar', 'Macedônia'),
                ('MMK', 'K', 'Kyat', 'Myanmar'),
                ('MNT', '₮', 'Tugrik', 'Mongólia'),
                ('MOP', 'P', 'Pataca', 'Macau'),
                ('MRU', 'UM', 'Ouguiya', 'Mauritânia'),
                ('MUR', '₨', 'Rupia de Maurício', 'República de Maurício'),
                ('MVR',	'ރ.', 'Rufiyaa', 'Maldivas'),
                ('MWK', 'MK', 'Kwacha', 'Malavi'),
                ('MXN', '$', 'Peso Mexicano', 'México'),
                ('MYR', 'RM', 'Ringgit Malaio', 'Malásia'),
                ('MZN', 'MTn', 'Metical', 'Moçambique'),
                ('NAD', '$', 'Dólar da Namíbia', 'Namíbia'),
                ('NGN', '₦', 'Naira', 'Nigéria'),
                ('NIO', 'C$', 'Oro de Cordoba', 'Nicarágua'),
                ('NOK', 'kr', 'Coroa Norueguesa', 'Noruega'),
                ('NPR', '₨', 'Rupia Nepalesa', 'Nepal'),
                ('NZD', '$', 'Dólar Neozelandês', '[Ilhas Cook, Nova Zelândia, Niue, Ilha Pitcairn]'),
                ('OMR',	'ر.ع.', 'Rial Omani', 'Omã'),
                ('PAB', 'B/.', 'Balboa', 'Panamá'),
                ('PEN', 'S/.', 'Novo Sol', 'Peru'),
                ('PGK', 'K', 'Kina', 'Papua Nova Guiné'),
                ('PHP', '₱', 'Peso Filipinio', 'Filipinas'),
                ('PKR', '₨', 'Rupia Paquistanesa', 'Paquistão'),
                ('PLN', 'zł', 'PZloty', 'Polônia'),
                ('PYG', '₲', 'Guarani', 'Paraguai'),
                ('QAR', 'ر.ق', 'Qatari Rial', 'Catar'),
                ('RON', 'L', 'Leu', 'Romênia'),
                ('RSD', 'din', 'Dinar Sérvio', '[Kosovo, Sérvia]'),
                ('RUB', 'р.', 'Rublo Russo', '[Rússia, Ossétia do Sul]'),
                ('RWF', '₣', 'Franco de Ruanda', 'Ruanda'),
                ('SAR',	'ر.س', 'Riyal Saudita', 'Arábia Saudita'),
                ('SBD', '$', 'Dólar das Ilhas Salomão', 'Ilhas Salomão'),
                ('SCR', '₨', 'Rúpia do Seicheles', 'Seicheles'),
                ('SDG', '£', 'Libra Sudanesa', 'Sudão'),
                ('SEK', 'kr', 'Coroa Sueca', 'Suécia'),
                ('SGD', '$', 'Dólar de Cingapura', '[Brunei, Cingapura]'),
                ('SHP', '£', 'Libra de Santa Helena', '[Ascension Island, Santa Helena, Tristan da Cunha]'),
                ('SLL', 'Le', 'Leone', 'Serra Leoa'),
                ('SOS', 'Sh', 'Shilling Somali', 'Somália'),
                ('SRD', '$', 'Dólar do Suriname', 'Suriname'),
                ('STN', 'Db', 'Dobra', 'São Tomé e Príncipe'),
                ('SYP', 'ل.س', 'Libra Síria', 'Síria'),
                ('SZL', 'L', 'Lilangeni', 'Suazilândia'),
                ('THB', '฿', 'Baht', 'Tailândia'),
                ('TJS', 'ЅМ', 'Somoni', 'Tajiquistão'),
                ('TMT', 'm', 'Manat', 'Turquemenistão'),
                ('TND', 'د.ت', 'Dinar Tunisiano', 'Tunísia'),
                ('TOP', 'T$', 'Pa’anga', 'Tonga'),
                ('TRY', '₤', 'Lira Turca', '[Chipre do Norte, Turquia]'),
                ('TTD', '$', 'Dólar de Trinidad e Tobago', 'Trinidad e Tobago'),
                ('TWD', '$', 'Dólar de Taiwan', 'Taiwan'),
                ('TZS', 'Sh', 'Shilling da Tanzânia', 'Tanzânia'),
                ('UAH', '₴', 'Hryvnia', 'Ucrânia'),
                ('UGX', 'Sh', 'Shilling de Uganda', 'Uganda'),
                ('USD', '$', 'Dólar Norte-Americano', '[Samoa Americana, Território Britânico do Oceano Índico, Ilhas Virgens Britânicas, Guam, Haiti, Marshall Islands, Micronésia, Ilhas Marianas do Norte, Ilhas Remotas do Pacífico, Palau, Panamá, Porto Rico, Ilhas Turcas e Caicos, Estados Unidos da América, Ilhas Virgens dos EE.UU.]'),
                ('UYU', '$', 'Peso Uruguaio', 'Uruguai'),
                ('UZS', 'лв', 'Sum Uzbequistão', 'Uzbequistão'),
                ('VEF', 'Bs F', 'Bolivar Venezuelano', 'Venezuela'),
                ('VND', '₫', 'Dong', 'Vietnã'),
                ('VUV', 'Vt', 'Vatu', 'Vanuatu'),
                ('WST', 'T', 'Tala', 'Samoa'),
                ('XAF', '₣', 'Franco CFA BCEAO', '[Benin, Burkina Faso, Camarões, República Central Africana, Chade, Congo (Brazzaville), Costa do Marfim, Guiné Equatorial, Gabão, Guiné-Bissau, Mali, Níger, Senegal, Togo]'),
                ('XCD', '$', 'Dólar do Caribe Oriental', '[Anguilla, Antigua and Barbuda, Dominica, Granada, Montserrat, São Cristóvão e Nevis, Santa Lúcia, São Vicente e Granadinas]'),
                ('XPF', '₣', 'Franco CFP', '[Polinésia Francesa, Nova Caledônia, Wallis e Futuna]'),
                ('YER', '﷼', 'Rial Iemnita', 'Iémen'),
                ('ZAR', 'R', 'Rand', '[Lesoto, Namíbia, África do Sul]'),
                ('ZMW', 'ZK', 'Kwacha Zambiano', 'Zâmbia'),
                ('ZWL', '$', 'Dólar do Zimbábue', 'Zimbábue'),
            ]

    return [data for data in coins if coin in data]
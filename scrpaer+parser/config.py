import io
from dataclasses import dataclass
from enum import Enum
from os import environ
from typing import Literal
from typing import Union

from dotenv import load_dotenv

# Charger les variables d'environnement a partir du fichier .env tous les call environ 
# Logging config parameters
# Browser init params


load_dotenv()


@dataclass

class SmartphoneUserAgent:
    user_agent: str #user_agent du smartphone
    device_metrics: dict[str, float]

#Literal: pour specifier le type de donnees dans la liste
class Config:
    # Logging config parameters
    logging_levels = Literal["TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"]
    logging_dumps = Union[str, io.TextIOWrapper]
    max_rotation_days = 10
    max_retention_days = 30

    # Browser init params
    headless: bool = (
        environ["HEADLESS"] == "YES" #Savoir si afficher interface graphique ou non
    )  # only use 'YES' or 'NO' for this variable in the .env / docker configs
    use_docker: bool = (
        environ["USE_DOCKER"] == "YES" #Savoir si il doit etre exceute dans un env docker ou non
    )  # only use 'YES' or 'NO' for this variable in the .env / docker configs
    chrome_path = environ["CHROME_PATH"]

    # Alcohol types
    alcohol_types = Literal[
        "beer",
        "wine",
        "whiskey",
        "juice",
        "vodka",
        "spirits",
        "red_wine",
        "white_wine",
        "rose_wine",
        "sparkling",
    ]

    # Amending alcohol categories for storage according to Dan Murphy's which serves as a reference
    danmurphys_alcohol_categories = Literal[
        "red_wine",
        "white_wine",
        "rose",
        "champagne",
        "fortified_wine",
        "whisky",
        "bourbon",
        "vodka",
        "gin",
        "tequila",
        "rum",
        "brandy_cognac",
        "liqueur",
        "aperitif",
        "other_spirits",
        "beer",
        "cider",
        "premix",
        "zero_wine",
        "zero_beer",
        "zero_spirits",
        "zero_premix",
        "zero_cider",
    ]

    # Default packaging
    DEFAULT_PACKAGING: dict[str, Literal["can", "bottle"]] = {
        "red_wine": "bottle",
        "white_wine": "bottle",
        "rose": "bottle",
        "champagne": "bottle",
        "fortified_wine": "bottle",
        "whisky": "bottle",
        "whiskey": "bottle",
        "vodka": "bottle",
        "bourbon": "bottle",
        "gin": "bottle",
        "tequila": "bottle",
        "rum": "bottle",
        "brandy_cognac": "bottle",
        "liqueur": "bottle",
        "aperitif": "bottle",
        "other_spirits": "bottle",
        "beer": "can",
        "cider": "bottle",
        "premix": "bottle",
        "zero_wine": "bottle",
        "zero_beer": "can",
        "zero_spirits": "bottle",
        "zero_premix": "bottle",
        "zero_cider": "bottle",
        "rose_wine": "bottle",
        "sparkling": "bottle",
    }
#Une liste de smartphoneUserAgent avec les objets de la classe SmartphoneUserAgent
    #### Smartphone user agents
    SMARTPHONE_USER_AGENTS = [
        SmartphoneUserAgent(
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1",
            device_metrics={"width": 375, "height": 812, "pixelRatio": 3.0},
        ),  # Iphone X
        SmartphoneUserAgent(
            user_agent="Mozilla/5.0 (Linux; Android 11; SM-A716B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
            device_metrics={"width": 412, "height": 869, "pixelRatio": 3.0},
        ),  # Samsung S9
        SmartphoneUserAgent(
            user_agent="Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
            device_metrics={"width": 360, "height": 720, "pixelRatio": 2.0},
        ),  # LG Stylo 5
        SmartphoneUserAgent(
            user_agent="Mozilla/5.0 (Linux; Android 11; HD1901) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
            device_metrics={"width": 1080, "height": 2340, "pixelRatio": 2.625},
        ),  # OnePlus 7T
        SmartphoneUserAgent(
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/90.0.4430.78 Mobile/15E148 Safari/604.1",
            device_metrics={"width": 375, "height": 812, "pixelRatio": 3.0},
        ),  # Iphone X
        SmartphoneUserAgent(
            user_agent="Mozilla/5.0 (Linux; Android 10; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
            device_metrics={"width": 360, "height": 760, "pixelRatio": 4.0},
        ),  # Samsung Galaxy S10
        SmartphoneUserAgent(
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/90.0.4430.78 Mobile/15E148 Safari/604.1",
            device_metrics={"width": 375, "height": 812, "pixelRatio": 3.0},
        ),  # Iphone X
        SmartphoneUserAgent(
            user_agent="Mozilla/5.0 (Linux; Android 11; SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
            device_metrics={"width": 412, "height": 869, "pixelRatio": 3.0},
        ),  # Samsung Note 20 Ultra
    ]

    NUM_SMARTPHONE_USER_AGENTS = len(SMARTPHONE_USER_AGENTS)

    UPDATED_USER_AGENTS = [
        {
            "percent": "22.1%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36",
            "system": "Chrome 112.0 Win10",
        },
        {
            "percent": "11.4%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36",
            "system": "Chrome 112.0 macOS",
        },
        {
            "percent": "7.8%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko\/20100101 Firefox\/112.0",
            "system": "Firefox 112.0 Win10",
        },
        {
            "percent": "5.4%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/113.0.0.0 Safari\/537.36",
            "system": "Chrome Generic Win10",
        },
        {
            "percent": "3.4%",
            "useragent": "Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36",
            "system": "Chrome 112.0 Linux",
        },
        {
            "percent": "3.1%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/111.0.0.0 Safari\/537.36",
            "system": "Chrome 111.0 Win10",
        },
        {
            "percent": "2.9%",
            "useragent": "Mozilla\/5.0 (X11; Linux x86_64; rv:109.0) Gecko\/20100101 Firefox\/112.0",
            "system": "Firefox 112.0 Linux",
        },
        {
            "percent": "2.2%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/113.0.0.0 Safari\/537.36",
            "system": "Chrome Generic macOS",
        },
        {
            "percent": "2.0%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/16.4 Safari\/605.1.15",
            "system": "Safari Generic macOS",
        },
        {
            "percent": "1.9%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko\/20100101 Firefox\/112.0",
            "system": "Firefox 112.0 macOS",
        },
        {
            "percent": "1.7%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; rv:112.0) Gecko\/20100101 Firefox\/112.0",
            "system": "Firefox 112.0 Win10",
        },
        {
            "percent": "1.4%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko\/20100101 Firefox\/113.0",
            "system": "Firefox Generic Win10",
        },
        {
            "percent": "1.3%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/111.0.0.0 Safari\/537.36",
            "system": "Chrome 111.0 macOS",
        },
        {
            "percent": "1.3%",
            "useragent": "Mozilla\/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko\/20100101 Firefox\/112.0",
            "system": "Firefox 112.0 Linux",
        },
        {
            "percent": "1.3%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36 Edg\/112.0.1722.58",
            "system": "Edge 112.0 Win10",
        },
        {
            "percent": "1.1%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko\/20100101 Firefox\/111.0",
            "system": "Firefox 111.0 Win10",
        },
        {
            "percent": "1.1%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36 Edg\/112.0.1722.48",
            "system": "Edge 112.0 Win10",
        },
        {
            "percent": "1.0%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/111.0.0.0 Safari\/537.36 OPR\/97.0.0.0",
            "system": "Chrome 111.0 Win10",
        },
        {
            "percent": "1.0%",
            "useragent": "Mozilla\/5.0 (X11; Linux x86_64; rv:102.0) Gecko\/20100101 Firefox\/102.0",
            "system": "Firefox 102.0 Linux",
        },
        {
            "percent": "0.9%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/109.0.0.0 Safari\/537.36",
            "system": "Chrome 109.0 Win10",
        },
        {
            "percent": "0.9%",
            "useragent": "Mozilla\/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/109.0.0.0 Safari\/537.36",
            "system": "Chrome 109.0 Win7",
        },
        {
            "percent": "0.8%",
            "useragent": "Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/111.0.0.0 Safari\/537.36",
            "system": "Chrome 111.0 Linux",
        },
        {
            "percent": "0.7%",
            "useragent": "Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/113.0.0.0 Safari\/537.36",
            "system": "Chrome Generic Linux",
        },
        {
            "percent": "0.7%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/113.0.0.0 Safari\/537.36 Edg\/113.0.1774.35",
            "system": "Edge Generic Win10",
        },
        {
            "percent": "0.7%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36 Edg\/112.0.1722.68",
            "system": "Edge 112.0 Win10",
        },
        {
            "percent": "0.6%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/16.3 Safari\/605.1.15",
            "system": "Safari Generic macOS",
        },
        {
            "percent": "0.6%",
            "useragent": "Mozilla\/5.0 (X11; Linux x86_64; rv:109.0) Gecko\/20100101 Firefox\/113.0",
            "system": "Firefox Generic Linux",
        },
        {
            "percent": "0.6%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36 Edg\/112.0.1722.64",
            "system": "Edge 112.0 Win10",
        },
        {
            "percent": "0.6%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/99.0.4844.51 Safari\/537.36",
            "system": "Chrome 99.0 Win10",
        },
        {
            "percent": "0.5%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; rv:102.0) Gecko\/20100101 Firefox\/102.0",
            "system": "Firefox 102.0 Win10",
        },
        {
            "percent": "0.5%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36 OPR\/98.0.0.0",
            "system": "Chrome 112.0 Win10",
        },
        {
            "percent": "0.4%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/110.0.0.0 Safari\/537.36",
            "system": "Chrome 110.0 Win10",
        },
        {
            "percent": "0.4%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko\/20100101 Firefox\/102.0",
            "system": "Firefox 102.0 Win10",
        },
        {
            "percent": "0.3%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/16.4.1 Safari\/605.1.15",
            "system": "Safari Generic macOS",
        },
        {
            "percent": "0.3%",
            "useragent": "Mozilla\/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36",
            "system": "Chrome 112.0 ChromeOS",
        },
        {
            "percent": "0.3%",
            "useragent": "Mozilla\/5.0 (X11; Linux x86_64; rv:109.0) Gecko\/20100101 Firefox\/111.0",
            "system": "Firefox 111.0 Linux",
        },
        {
            "percent": "0.3%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko\/20100101 Firefox\/111.0",
            "system": "Firefox 111.0 macOS",
        },
        {
            "percent": "0.3%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko\/20100101 Firefox\/114.0",
            "system": "Firefox Generic Win10",
        },
        {
            "percent": "0.3%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko\/20100101 Firefox\/113.0",
            "system": "Firefox Generic macOS",
        },
        {
            "percent": "0.3%",
            "useragent": "Mozilla\/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko\/20100101 Firefox\/112.0",
            "system": "Firefox 112.0 Win7",
        },
        {
            "percent": "0.3%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36 Edg\/112.0.1722.39",
            "system": "Edge 112.0 Win10",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) SamsungBrowser\/20.0 Chrome\/106.0.5249.126 Safari\/537.36",
            "system": "Chrome Generic Linux",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/110.0.0.0 Safari\/537.36",
            "system": "Chrome 110.0 macOS",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/16.2 Safari\/605.1.15",
            "system": "Safari 16.2 macOS",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (Windows NT 6.1; rv:102.0) Gecko\/20100101 Goanna\/6.0 Firefox\/102.0 PaleMoon\/32.0.0",
            "system": "PaleMoon Generic Win7",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko\/20100101 Firefox\/111.0",
            "system": "Firefox 111.0 Linux",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/108.0.0.0 Safari\/537.36",
            "system": "Chrome 108.0 macOS",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/79.0.3945.88 Safari\/537.36",
            "system": "Chrome 79.0 macOS",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; rv:111.0) Gecko\/20100101 Firefox\/111.0",
            "system": "Firefox 111.0 Win10",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; rv:113.0) Gecko\/20100101 Firefox\/113.0",
            "system": "Firefox Generic Win10",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/110.0.0.0 YaBrowser\/23.3.3.719 Yowser\/2.5 Safari\/537.36",
            "system": "Yandex Browser Generic Win10",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/16.1 Safari\/605.1.15",
            "system": "Safari 16.1 macOS",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/108.0.0.0 Safari\/537.36",
            "system": "Chrome 108.0 Win10",
        },
        {
            "percent": "0.2%",
            "useragent": "Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/108.0.0.0 Safari\/537.36",
            "system": "Chrome 108.0 Win10",
        },
    ]

    NUM_UPDATED_USER_AGENTS = len(UPDATED_USER_AGENTS)

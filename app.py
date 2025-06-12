from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -----------------------------
# Dummy Login Function
# -----------------------------
def check_login(phone, password):
    return phone == "1234567890" and password == "password"

# -----------------------------
# Gift Data
# -----------------------------
gifts_data = {
    "Toy Car": {
        "image": "https://m.media-amazon.com/images/I/41wBaViokKL._SX300_SY300_QL70_FMwebp_.jpg",
        "amazon": {"link": "https://www.amazon.in/...", "price": 399},
        "flipkart": {"link": "https://www.flipkart.com/...", "price": 282}
    },
    "Doll Set": {
        "image": "https://m.media-amazon.com/images/I/814XPCZPbxL._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/...", "price": 249},
        "flipkart": {"link": "https://www.flipkart.com/...", "price": 320}
    },
    "Watch": {
        "image": "https://rukminim2.flixcart.com/image/612/612/xif0q/smartwatch/p/l/f/-original-imah4nbw8dmxhhh6.jpeg?q=70",
        "amazon": {"link": "https://www.amazon.in/...", "price": 2999},
        "flipkart": {"link": "https://www.flipkart.com/...", "price": 2299}
    },
    "LEGO Set": {
        "image": "https://m.media-amazon.com/images/I/817z8SudAqL._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/LEGO-Technic-Heavy-Duty-Bulldozer-42163/dp/B0CFVN4XVL/ref=sr_1_33?crid=NZMTTNHPXG0M&dib=eyJ2IjoiMSJ9.4QTCQB5puVhEPwAzRzp0v-MEG_EBnKjsy4tHI_A4fDNbyWCHXx5xRuLJlR22QDI26T5LSFQwxSRZ8lh6MV_SsZ5xZdvzuPgW2hXo9d6kOdMfQVddRuPXlZ4hrsGfqIEvkyjLZWB6mnT7U5R4MWKVXli-N4YNW7EPaZH7Cfn-V1sBLg0OzLGnFytHHT6fYZYgbzsPtCbrQmyvuw1lZJfsR2M9MHiScPjtqa7phngvk7xoQneeX58Q0eXvLjgO2OUnUaYBG4Qb1dNh2aiAirh6o9LiyXJandiPTaLjoyuCFvE.yN0OaqBHtHYzZAL7r8iZRgaCey6EvhTqK_UmpGCjgk0&dib_tag=se&keywords=lego+set&nsdOptOutParam=true&qid=1748426252&sprefix=lego+set%2Caps%2C238&sr=8-33", "price": 1090},
        "flipkart": {"link": "https://www.flipkart.com/lego-technic-heavy-duty-bulldozer-set-42163-195-pieces/p/itma99cac7e6131f?pid=BLCGWGXT5G4Q2HFU&lid=LSTBLCGWGXT5G4Q2HFUOZQBKJ&marketplace=FLIPKART&q=lego+set&store=tng%2Fll1%2Fe5o&srno=s_1_7&otracker=search&otracker1=search&fm=Search&iid=c853485b-ed35-470c-82d3-85eacf4962f6.BLCGWGXT5G4Q2HFU.SEARCH&ppt=sp&ppn=sp&ssid=o76jxs06rk0000001748426266502&qH=744923a9fbcb35fa", "price": 1090}
    },
    "Superhero Costume": {
        "image": "https://m.media-amazon.com/images/I/41JSsISA93L._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/sspa/click?ie=UTF8&spc=MTozNjY2Nzg5NjQ0NDQ1MjE5OjE3NDg0MjY3ODM6c3BfYXRmOjMwMDQ4MjUwMzA2MDMzMjo6MDo6&url=%2FMODERNAZ-Polyester-Superhero-Spiderboy-Multicolor%2Fdp%2FB0D1VXMQC9%2Fref%3Dsr_1_3_sspa%3Fcrid%3D2XRTH68LSLQ51%26dib%3DeyJ2IjoiMSJ9.OxbCj-w7XQOrXx11TR4UQkIGHCkNsFHO3NK9dFC9ZYhceXBfVluIE85bbYXB06JxHNMI0A7vuVFZL-Zml3AGA7lcafbir2Eaiu9Sh6II65SjAbqkz-K-xZDx5wG3PwauadUdxcnx6c25hByBSmRNI7tsC4PJf6nNZCdiGKy4gw4P7ns8vKqVAE863wzm6JVjrMXo9ahc2GJOXlOzzQqQnTltLlf3k88gxyxK4QCRPkW_PMs_TgCCYiDHaNGuAZxG5sVYepW2bpOsS3ibXyDLxf3efJ2Oi8RApAa5R4-7i-E.8RKtESHUx746fiyzL4iOPUzlkowmFa-WwROKIVVbBCw%26dib_tag%3Dse%26keywords%3Dsuper%2Bhero%2Bcostume%26qid%3D1748426783%26sprefix%3Dsuper%2Bhero%2Bcustom%252Caps%252C289%26sr%3D8-3-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1", "price":289},
        "flipkart": {"link": "https://www.flipkart.com/urika-superheroes-kids-costume-wear/p/itm322446aecfd62?pid=KCWGHGASHUYVTYMQ&lid=LSTKCWGHGASHUYVTYMQDKHQU6&marketplace=FLIPKART&q=Super+Hero+Custome&store=clo%2Feof%2Fygv&srno=s_1_8&otracker=search&otracker1=search&fm=Search&iid=0c249d7a-71ef-4282-a566-a660657afb04.KCWGHGASHUYVTYMQ.SEARCH&ppt=sp&ppn=sp&ssid=snvuqb2bxc0000001748426800937&qH=80435a0f7af7d169", "price":200}
    },
    "RC Helicopter": {
        "image": "https://rukminim2.flixcart.com/image/612/612/xif0q/remote-control-toy/8/v/6/rc-helicopter-with-hand-gravity-sensor-flying-remote-control-original-imahamkpyvxcstga.jpeg?q=70",
        "amazon": {"link": "https://www.amazon.in/sspa/click?ie=UTF8&spc=MTo1NTE3ODM5MjgyMjg5MjExOjE3NDg0MjcwMTk6c3Bfc2VhcmNoX3RoZW1hdGljOjMwMDUzMjQ2MjQ1MzgzMjo6Mjo6&url=%2FKIDZYMON%25C2%25AE-Control-Charging-Helicopter-Included%2Fdp%2FB0F3V6P118%2Fref%3Dsxin_15_pa_sp_search_thematic_sspa%3Fcontent-id%3Damzn1.sym.739e670d-dfb3-4be0-9815-d8c5c0372e07%253Aamzn1.sym.739e670d-dfb3-4be0-9815-d8c5c0372e07%26crid%3D3K5EA8VKGA6DV%26cv_ct_cx%3DRC%2BHelicopter%26keywords%3DRC%2BHelicopter%26pd_rd_i%3DB0F3V6P118%26pd_rd_r%3D95cd31be-636d-4783-9c66-fb4f19785f19%26pd_rd_w%3Deg3HL%26pd_rd_wg%3DCku6w%26pf_rd_p%3D739e670d-dfb3-4be0-9815-d8c5c0372e07%26pf_rd_r%3DJZNB57YSS5PE4R0BDHV7%26qid%3D1748427019%26sbo%3DRZvfv%252F%252FHxDF%252BO5021pAnSA%253D%253D%26sprefix%3Drc%2Bhelicopter%252Caps%252C406%26sr%3D1-3-66673dcf-083f-43ba-b782-d4a436cc5cfb-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM%26psc%3D1", "price":390},
        "flipkart": {"link": "https://www.flipkart.com/exaltedcollection-toy-helicopter-kids-easy-control-rc-helicopter-great-gift-boys-girls/p/itm0a2626582ca5f?pid=RCTHBTEDAZABQDQU&lid=LSTRCTHBTEDAZABQDQUX9ZZWU&marketplace=FLIPKART&q=RC+Helicopter&store=tng%2F56a%2Ffq8&srno=s_1_5&otracker=search&otracker1=search&fm=Search&iid=14bced11-1036-4484-947d-30492f858529.RCTHBTEDAZABQDQU.SEARCH&ppt=sp&ppn=sp&ssid=5hibi3s5cw0000001748427024806&qH=c5962e5006871302", "price":380}
    },
    "Puzzle Game": {
        "image": "https://m.media-amazon.com/images/I/91ussIbOplL._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/Funskool-Educational-Learning-Development-Childrens/dp/B00ELBBGOI/ref=sr_1_26?crid=28FPR8JIDB0XV&dib=eyJ2IjoiMSJ9.8eCbnzdpnq5gKHq25YutiSvjlXvHro8fdgrqNjlWR5WOzeKgveAI8xq8mNq96zAgxWpttkkGDX_JzfZbPD3QkUxQJo_26lhEzNfA7RkH0DNahSjG7ikgtgl6q8iDS7lC-K7rqVtvn8iwrUnK5QhNmJDR50TMUB18KE6S9rcoDDZeVYorXiyT691_gGfqwRoFu_6fI5KemH28NFqa5ltXgPg6msJBpOFhFmyHFEVl9moqzG2-21BnqRUID2pxjlY9hjTgifMmVVAgz1D4W6W0FDog_5NDKNfg-bMrWJD2q80.uWa2GlnyWHxpYHEKA69Q9d5ZX96PkxV37lJqMDQ6uoY&dib_tag=se&keywords=Puzzle+Game&qid=1748427160&sprefix=puzzle+game%2Caps%2C517&sr=8-26", "price":225},
        "flipkart": {"link": "https://www.flipkart.com/funskool-india-map-puzzles-learning-game/p/itmdx92ff7zfheq2?pid=PUZDX92FAMNZHYKY&lid=LSTPUZDX92FAMNZHYKYNQ2QW9&marketplace=FLIPKART&q=Puzzle+Game&store=tng%2Fkk6&srno=s_1_5&otracker=search&otracker1=search&fm=Search&iid=f2fcffd3-1d22-4c98-a606-b344647d8296.PUZDX92FAMNZHYKY.SEARCH&ppt=sp&ppn=sp&ssid=0alh3nk3j40000001748427163785&qH=575b69c9aadd8fd1", "price":180}
    },
    "Coloring Kit": {
        "image": "https://m.media-amazon.com/images/I/71FN+qOCJlL._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/sspa/click?ie=UTF8&spc=MTo0ODgzNDk1MjA3MTIwMzM0OjE3NDg0MjczNDI6c3BfYXRmOjMwMDQ2MzY4MTA4NDQzMjo6MDo6&url=%2FCrazyMart-Professional-Set-145-Watercolour%2Fdp%2FB0DQXNNTPB%2Fref%3Dsr_1_3_sspa%3Fcrid%3D6G7NWNYPTJ5%26dib%3DeyJ2IjoiMSJ9.ywTKU8h8CQSug-Rkqqxf-qBuJSx9gvXSBE_i6iwFn3hovX4PrdZH10d-QKx7LNcwk5JX3RaVGiVceKR_FU_dG5hSB0NmbsXL12j0ikfnwxBhUVReZV_C3hWY5v_G0JDx9u_t11FA3hOIGRVuAfchpJLx1fsJRnCLdOR5A0RBWLOHFxBs8ueKe_F8ZWTQo2DZYQp6THPD_KBz63RvggXgneQ4v9s6vIfv2aBe4Zds9hdW-e_uKc11NQraNBwEnY7lLQFQ04Y111QSVNzbLQ1w8TjhSaBVxzPTrqXXq0i7OX8.OVfdseSG8AhCeJnAETiBOjcSUsfVYLHu9aQXs7SL0p8%26dib_tag%3Dse%26keywords%3DColoring%2BKit%26qid%3D1748427342%26sprefix%3Dcoloring%2Bkit%252Caps%252C395%26sr%3D8-3-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1", "price":1140},
        "flipkart": {"link": "https://www.flipkart.com/kidziit-colour-set-unicorn-color-box/p/itmaa1501c11653c?pid=ARTGUZGS2SNZBFZN&lid=LSTARTGUZGS2SNZBFZN7UMXMG&marketplace=FLIPKART&q=Coloring+Kit&store=search.flipkart.com&srno=s_1_6&otracker=search&otracker1=search&fm=Search&iid=4ad5f141-f093-4641-8a24-90997876c896.ARTGUZGS2SNZBFZN.SEARCH&ppt=sp&ppn=sp&ssid=qtjohm0kw00000001748427347085&qH=090825471d676b4e", "price":950}
    },
    "Story Book": {
        "image": "https://m.media-amazon.com/images/I/81q77Q39nEL._AC_UY327_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/Harry-Potter-Philosophers-Stone-Rowling/dp/1408855658/ref=sr_1_1?crid=183IBY0SQKVQT&dib=eyJ2IjoiMSJ9.HhBPxSMP_TbUZVX2bgMG18OJVRei45Gt07oUgKTqj1S8StHkJa9xH31jCtGAUAWTMbK074fff076S1vut1MiGpZXTK4rBqKsKCdwj1x8uYVDAp31htTDfrvk5wBFkPtipdORlwA8f6rDdem30OrXDKmQO6r7JDIbxX8HGBFAkKTbt38YzMSit4ELaYeOWgZ6sPuThEpAwkYRx8VosBYxbZf8B3I0TMCDHZXvegEo_Oc.Rpgm7nxA0GUUCJ5SAE6t-fIk4BvaIleU8xArW5xLJhI&dib_tag=se&keywords=Story+Book+harry+potter&qid=1748427539&sprefix=story+book+harry+potter%2Caps%2C273&sr=8-1", "price":370},
        "flipkart": {"link": "https://www.flipkart.com/harry-potter-philosopher-s-stone/p/itmfc5dhvrkh5jqp?pid=9781408855652&lid=LSTBOK9781408855652ESKBPF&marketplace=FLIPKART&q=Story+Book&store=bks&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=3ebde3f9-7008-4fd5-931e-10f22d42176f.9781408855652.SEARCH&ppt=sp&ppn=sp&ssid=hd7xkd0lxc0000001748427488037&qH=c3e3a0add5f5c52d", "price":290}
    },
    "Princess Tent": {
        "image": "https://m.media-amazon.com/images/I/712CYrqh+hS._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/sspa/click?ie=UTF8&spc=MTo2MzE5MDQ2NTQyNjQ3Njk1OjE3NDg0Mjc2Nzg6c3Bfc2VhcmNoX3RoZW1hdGljOjMwMDU2MTg3MDk5OTczMjo6Mjo6&url=%2FRoyal-Jumbo-Extremely-Light-Weight%2Fdp%2FB0F4CP6RXW%2Fref%3Dsxin_15_pa_sp_search_thematic_sspa%3Fcontent-id%3Damzn1.sym.739e670d-dfb3-4be0-9815-d8c5c0372e07%253Aamzn1.sym.739e670d-dfb3-4be0-9815-d8c5c0372e07%26crid%3D1G9J73X7WK876%26cv_ct_cx%3DPrincess%2BTent%26keywords%3DPrincess%2BTent%26pd_rd_i%3DB0F4CP6RXW%26pd_rd_r%3D98d504e9-bd4a-416c-a0e5-783b0d916a95%26pd_rd_w%3D50tEX%26pd_rd_wg%3DXSfqp%26pf_rd_p%3D739e670d-dfb3-4be0-9815-d8c5c0372e07%26pf_rd_r%3DRT69AX1RPRQ5TXQ3VEDE%26qid%3D1748427678%26sbo%3DRZvfv%252F%252FHxDF%252BO5021pAnSA%253D%253D%26sprefix%3Dprincess%2Btent%252Caps%252C260%26sr%3D1-3-66673dcf-083f-43ba-b782-d4a436cc5cfb-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM%26psc%3D1", "price":499},
        "flipkart": {"link": "https://www.flipkart.com/cloudtech-big-size-play-tent-house-boys-girls/p/itm9aabcf287a515?pid=OTYGSFSTDDEQEYSS&lid=LSTOTYGSFSTDDEQEYSS6ZBK9J&marketplace=FLIPKART&q=Princess+Tent&store=tng%2Flhf%2Fazy&srno=s_1_6&otracker=search&otracker1=search&fm=Search&iid=en_9r-_dtl4fPX6GPCYY4X-fuIwr3WPF_NI34FXmdj8uvqh0ikj2Oy1Pw_hj9_ed1IMT5duBabxl-K9nhjJ_WIT0Q%3D%3D&ppt=sp&ppn=sp&ssid=njbf9gwcw00000001748427672202&qH=a9fad06f903228d0", "price":450}
    },
    "DIY Bracelet Kit": {
        "image": "https://m.media-amazon.com/images/I/81rVw7zoDrL._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/Satmarhz-Bracelet-Making-Jewellery-Birthday/dp/B0CXHP8FG2/ref=sr_1_5?crid=3KZY082HXA0VB&dib=eyJ2IjoiMSJ9.55pHV5Bl2ptwf2JrylhDunRz5jAcbs5-XKiFVvyfzFSCzfy7d3VidUkDHJjRlUiWBKbwKRVcuuEIMagBsRSDQkl_Je3UzkcLf6c5jBDyC1y05c1o-rGIYnF3TWbIKH9Zz-ckx6F8fhp84gHP06_g_QNNgXylyf_HL9scrd7OK1y1KgHgPRv1lHbsudPL3l4jwoAp_2YAU3iDY8hNPLG_s-O_kuHQ4gQv02FkZX7e6rvfMr2gPjPvgctL2-a_kGB9MC08ElGalkxUneDz2A-nc0mRO-FRTq5vQJTEDvHHsYs.TBK4ix9Pkg_y3_QMMp6xIUB0V2tTyVPu6i_c8dVwXmk&dib_tag=se&keywords=DIY+Bracelet+Kit&qid=1748427792&sprefix=diy+bracelet+kit%2Caps%2C269&sr=8-5", "price":500},
        "flipkart": {"link": "https://www.flipkart.com/trexee-unicorn-bracelet-making-kit-girls-jewellery-kids-diy/p/itm4696daea2225b?pid=ACKH8CJYZHNTPGWU&lid=LSTACKH8CJYZHNTPGWUCFWLVK&marketplace=FLIPKART&q=DIY+Bracelet+Kit&store=tng%2Fcg5%2Ftzr&spotlightTagId=default_TrendingId_tng%2Fcg5%2Ftzr&srno=s_1_9&otracker=search&otracker1=search&fm=Search&iid=3904f50a-0758-4070-a0cc-4ad0dfe0d50d.ACKH8CJYZHNTPGWU.SEARCH&ppt=sp&ppn=sp&ssid=ofu8sxf2yo0000001748427785907&qH=61933696c7445dd1", "price":435}
    },
    "Gaming Mouse": {
        "image": "https://rukminim2.flixcart.com/image/612/612/xif0q/mouse/j/g/7/spectre-3600-dpi-gaming-sensor-and-7-colours-rainbow-lighting-original-imah92ay6qxxhw8k.jpeg?q=70",
        "amazon": {"link": "https://www.amazon.in/EvoFox-Spectre-Lighting-Breathing-White/dp/B0DGVH47HW/ref=sr_1_8?crid=2CI1R9RWL5WDU&dib=eyJ2IjoiMSJ9.0f2xXH20-jWnCAC3dFnR7hsSayf3b5w1qbPJ7i6vpEqyGE89o0-k2Ha5G4t0mNRDhCrMef39DPvmJmSPcOzVKrfPw6oXqQ3oVv8hXAsMewPa3LfpA1xejVgOIMl2s_cYRrZRxksuyzuVnsf1Y8lIxQW4HX7c5Z6RkOJL5Ol8jv3mvR5MFJYHvPIDjSXUV1Y1XkHZhV3x7UUVq9Kq0c9Rnd26ye_GCv1bhMJB-HSNeNg.gNUMJTnN0IcuVvTfU2MCHby9ZW0n68lmwxImSq7B6zc&dib_tag=se&keywords=Gaming+Mouse&qid=1748427961&sprefix=diy+bracelet+kit%2Caps%2C1627&sr=8-8", "price":379},
        "flipkart": {"link": "https://www.flipkart.com/evofox-spectre-3600-dpi-gaming-sensor-7-colours-rainbow-lighting-wired-ambidextrous-optical-mouse/p/itm790bab51b0d28?pid=ACCH6CGFJ8VHCMGW&lid=LSTACCH6CGFJ8VHCMGWYLUKBX&marketplace=FLIPKART&q=Gaming+Mouse&store=6bo%2Fai3%2F2ay&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=21ab52e0-e35b-4ab3-885b-cdb61ab35b5e.ACCH6CGFJ8VHCMGW.SEARCH&ppt=sp&ppn=sp&ssid=qwmpuhgq4g0000001748427964744&qH=0c4c9b8a3eb674e2", "price":380}
    },
    "Bluetooth Speaker": {
        "image": "https://m.media-amazon.com/images/I/61GKAEg1+FL._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/sspa/click?ie=UTF8&spc=MToxMDUyNjQyNTE5ODE4Njc1OjE3NDg0MjgwNjU6c3Bfc2VhcmNoX3RoZW1hdGljOjMwMDUxMjcwMzU1MjgzMjo6Mzo6&url=%2FEnterprises-Wireless-Microphone-Bluetooth-Entertainment%2Fdp%2FB0DRJ5CN9G%2Fref%3Dsxin_15_pa_sp_search_thematic_sspa%3Fcontent-id%3Damzn1.sym.739e670d-dfb3-4be0-9815-d8c5c0372e07%253Aamzn1.sym.739e670d-dfb3-4be0-9815-d8c5c0372e07%26crid%3DG56R7GX70YVM%26cv_ct_cx%3DBluetooth%2BSpeaker%26keywords%3DBluetooth%2BSpeaker%26pd_rd_i%3DB0DRJ5CN9G%26pd_rd_r%3Dcf328da0-a8c7-4431-94f6-e08df2fa0ef8%26pd_rd_w%3Dj3Otu%26pd_rd_wg%3DdFri7%26pf_rd_p%3D739e670d-dfb3-4be0-9815-d8c5c0372e07%26pf_rd_r%3D2GFMD3EV619ZWSH648TP%26qid%3D1748428065%26sbo%3DRZvfv%252F%252FHxDF%252BO5021pAnSA%253D%253D%26sprefix%3Dbluetooth%2Bspeaker%252Caps%252C302%26sr%3D1-4-66673dcf-083f-43ba-b782-d4a436cc5cfb-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM%26psc%3D1", "price": 496},
        "flipkart": {"link": "https://www.flipkart.com/seashot-google-alexa-siri-assistant-smart-speaker/p/itm7f74b8f3afa7b?pid=ACCH3SBFQEYUYQJN&lid=LSTACCH3SBFQEYUYQJNDKGRC6&marketplace=FLIPKART&q=Bluetooth+Speaker&store=0pm%2F0o7&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=3a959215-1697-4062-b6e6-41b1ab578d7f.ACCH3SBFQEYUYQJN.SEARCH&ppt=sp&ppn=sp&ssid=tl7l4gl19s0000001748428060969&qH=5e7677ee9b77825b", "price":440}
    },
    "Skateboard": {
        "image": "https://m.media-amazon.com/images/I/614v1krl0DL._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/Sell-Skateboard-Complete-Skateboards-Beginners/dp/B09Q5KHRQH/ref=sr_1_18?crid=7IQGHW3J8RNH&dib=eyJ2IjoiMSJ9.pAgVV6UkGuxHgDP8jF7aOKuSFjdyFvyDlp_2uxeK3mf15Y-4PoVMLmx41lTBHG4LopHH3HE7r2GT6bEessVCpjFCV7Su0_KZ6DPWjjhHHA-_c04U7I3Dnu9NFJMyJFumkOnYbQkCwcu1Mmr0dYse0iC1B_B1tjjoIs1l_qe40nPa_t2BJ_Zyhg9Es8MzOrHkKHRNfOsAhbhiUvucdOBI4jfuePVPuiWZt_58IiiqYPTplKwoDPIPFrxGzjPfBfgFJtThNhsZUGHq7h-FEGLyKsRAILDRpMHjQ4-tV3mM6yQ.rcE5zMwhEqX1i3lvp1bxUvZ8HZUQWb1a-JDTLJHR0Bc&dib_tag=se&keywords=Skateboard&qid=1748428182&sprefix=skateboard%2Caps%2C297&sr=8-18", "price":699},
        "flipkart": {"link": "https://www.flipkart.com/p-paytag-24-x-6-inch-dimond-kids-beginners-adult-multicolor-pack-1-skateboard/p/itmf07576498bb3a?pid=SKDGSRBTBS9BA7MZ&lid=LSTSKDGSRBTBS9BA7MZJRSERY&marketplace=FLIPKART&q=Skateboard&store=abc%2Fmgq%2Ftp8&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=en_UeJa3nOoQ2-RnsuiuKRuMy_e1q2sJk4dBLe7szmSvxSFcHXHJ8TfB7DgoKCqMMfvMnY0SMZdUYQWgDaVtidEbw%3D%3D&ppt=sp&ppn=sp&ssid=z8kfbqxids0000001748428177522&qH=974a2f9de4ff993f", "price":660}
    },
    "Football": {
        "image": "https://rukminim2.flixcart.com/image/612/612/xif0q/ball/t/f/w/420-470-storm-football-size-5-5-68-1-32-football-nivia-original-imah8epbhb4qyfpw.jpeg?q=70",
        "amazon": {"link": "https://www.amazon.in/Nivia-Storm-Football-Size-White/dp/B00ICCYF0E/ref=sr_1_5?crid=1C3BNVS3IWBF6&dib=eyJ2IjoiMSJ9.AUCem4LllOtEeHESqVbmNWvnlp6UsO7clR9k_EuHkLcW4aeDMCFKiR1UaygnARQLaTcXe0Cd-XHyFefAPV66UZstiRr7ObrXL_LboZbpe9-_r6OSgP4hK6cM8N3COxf-hXIn_a7JcKZtYRuAcoRgDPKRzqeSCp5ac8r458NWOTQF7T-iuojkbiV97LVl9iJpEzHpfjoBC6-cZQ1e6msu9pEdrKu2fZHWdYnn3HJbOqBywWzcV5OxaSf4cRHrC8hhAd8krPkVT9xZQZAkJlzpxWs28Eg6wc45zRFilhH-KTs.8IzENYxHCLmsuD8kVzgL6KQH0bIKBXwvNv2XZoKjWIk&dib_tag=se&keywords=Football&qid=1748428492&sprefix=football%2Caps%2C417&sr=8-5", "price":349},
        "flipkart": {"link": "https://www.flipkart.com/nivia-storm-football-size-5/p/itmf9ghrrzqmcshu?pid=BALDM4Q59MU5ZHNS&lid=LSTBALDM4Q59MU5ZHNSLWFXPW&marketplace=FLIPKART&q=Football&store=abc%2Fgxg&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=en_dWVpSqB-Y_SWpjHGdFpP5ifmYl8dl5KPqiF5aH-eEnERvADGwWgd3ETWzj9cRsmfZaXykwyYO6qzuhbwj8pDH_UFjCTyOHoHZs-Z5_PS_w0%3D&ppt=sp&ppn=sp&ssid=nmmn7p99680000001748428496817&qH=449a5f6d01d5f416", "price":350}
    },
    "Wireless Earbuds": {
        "image": "https://m.media-amazon.com/images/I/713Lr2oNWaL._AC_UY327_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/boAt-Airdopes-91-Prime-Bluetooth/dp/B0DPWL48Z5/ref=sr_1_6?crid=3ATVSLI4KIU3T&dib=eyJ2IjoiMSJ9.7_HIP__uYkNDL72wVFkwnM5Msu-Vm1zptkiLXnadhP2Z_zL6v4_edob31QhiU__lxFQphcAKsXLgfwE39EsHpR_xT7SIC4IdCwo5pGTNyltsy-XTMMbwouJnDmNz9c9Dk8ADKUIBpNX_YsqBtRjou2_wNrI5fOcKGw9pQhgwkZ74Zf6-tbM1hQJlge8J_prMv8YSiWLuqDsCl6_I2Nrio5T_ptzZ-fupjjIFkQDDFmg.iHunxNeufw-UVs9gqcI1u61k0we6ApXShW57s_fQFu8&dib_tag=se&keywords=Wireless+Earbuds&qid=1748428629&sprefix=wireless+earbuds%2Caps%2C595&sr=8-6", "price":749},
        "flipkart": {"link": "https://www.flipkart.com/boat-airdopes-91-bluetooth/p/itma32a259e45d62?pid=ACCH5FKQRGV2J8NJ&lid=LSTACCH5FKQRGV2J8NJXA3C6K&marketplace=FLIPKART&q=Wireless+Earbuds&store=0pm%2Ffcn%2F821%2Fa7x&srno=s_1_23&otracker=search&otracker1=search&fm=Search&iid=4727324b-cad0-4642-825d-c9cecaa5768c.ACCH5FKQRGV2J8NJ.SEARCH&ppt=sp&ppn=sp&ssid=rllcix0q800000001748428633404&qH=44d37d8a5eea9f68", "price":800}
    },
    "Makeup Kit": {
        "image": "https://m.media-amazon.com/images/I/71dTBrDQVqL._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/ZUKRAVE-Waterproof-Eyeshadow-Eyelashes-Foundation/dp/B0DMNCTVD4/ref=sr_1_14?crid=2CIY0YVM4N38I&dib=eyJ2IjoiMSJ9.C2ltLXnto1BLAvq2g3vmndTU4hse3RTMuR95Q5GlDcCqh1ogTwrhhLihQLoGwjILIyrKsQdwz6qyJd2uIhgZ4OElRJkofW_STKA5CS6Hk8lkBiAN9q2B32Hxcns5zaCbicK0ko2wAFVmJCr41JZ7pGIfbn6v3R1tA5eCEMEDe0KwC0tjlhUKEl_XfcpmTWRnlttGYJOl8PsNAebncpJAHas-7boByKwofnKCxq_NZ8sHs6BJ4VtHlvUC3bWn3N_RwcwucOcjF-jbg7FqTEYpWPJmCOzbnMIOwyqnpqOI5hg.bKHu_5Xf5DcjuNR2Cx_0J-ZoHSspTlg3-oz3JXk6n0E&dib_tag=se&keywords=Makeup+Kit&qid=1748428749&sprefix=makeup+kit%2Caps%2C399&sr=8-14", "price":549},
        "flipkart": {"link": "https://www.flipkart.com/jusbe-u-waterproof-makeup-kit-full-set-box-women-girls-13-items-set/p/itma8f2f3daaf707?pid=MKTHC7AGBQ82F9AH&lid=LSTMKTHC7AGBQ82F9AHSCMMFQ&marketplace=FLIPKART&q=Makeup+Kit&store=g9b%2Fffi&srno=s_1_8&otracker=search&otracker1=search&fm=Search&iid=ea300ff9-6b6b-4fc5-a87f-9741423b6e67.MKTHC7AGBQ82F9AH.SEARCH&ppt=sp&ppn=sp&ssid=lfck2ypxcw0000001748428753472&qH=de7563532a356ae4", "price":500}
    },
    "Instant Camera": {
        "image": "https://m.media-amazon.com/images/I/616XT1cN-XL._AC_UY327_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/Fujifilm-Mini-11-Instant-Happiness/dp/B094MZ45BV/ref=sr_1_3?crid=3C8NQKZ567NCY&dib=eyJ2IjoiMSJ9.P9X0JMTL1T5Ghw_4URQ0z2YimxaRnt7hKg9StZMhaexzOKGEku8miFs6F_mqVse-jXtThGq1WmExEy_UqyWIDcrqx3mwrdAqXYRtwiwsCU3AzOheqj-dGCpK43_Tg0k3VMsbUmLWSdG60cvqR-4s3SCnLFUMi6f4ETp8m9yjs1JJTeDoNJvC2vXqOXUvEqAsNhCejpcLhjJQ9hr2SXz5_KqrHqVXhaCXd5lKpM7AeNE.7lL2h6ea8i4hY402tQWS7hTOTW76FTksRCCnG9GGdJw&dib_tag=se&keywords=Instant+Camera&qid=1748428844&sprefix=makeup+kit%2Caps%2C266&sr=8-3", "price":8500},
        "flipkart": {"link": "https://www.flipkart.com/fujifilm-instax-treasure-box-mini-11-instant-camera/p/itme77e0804bcc36?pid=INAG37FNY2WHY9XG&lid=LSTINAG37FNY2WHY9XGLEXRCE&marketplace=FLIPKART&q=Instant+Camera&store=jek%2Fp31%2Fysu&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=360c9b02-7948-4c31-a9ad-83a8552de710.INAG37FNY2WHY9XG.SEARCH&ppt=sp&ppn=sp&ssid=3rpwum6nv40000001748428837848&qH=84c5cdd4c3875319", "price":6500}
    },
    "Selfie Ring Light": {
        "image": "https://rukminim2.flixcart.com/image/612/612/l4iscy80/flash/ring-flash/k/x/5/10-ring-light-with-camera-stand-7-ft-for-reels-video-stream-and-original-imagfefz4rgnsvjh.jpeg?q=70",
        "amazon": {"link": "https://www.amazon.in/sspa/click?ie=UTF8&spc=MTo2ODQxNjkwMTgzNTEwMzczOjE3NDg0Mjg5NTM6c3BfYXRmOjMwMDA0MTI4Mjk1OTIzMjo6MDo6&url=%2FTygot-YouTube-Shooting-Foldable-Lightweight%2Fdp%2FB08MCD9JFY%2Fref%3Dsr_1_1_sspa%3Fcrid%3D3FKUDTXIINWC7%26dib%3DeyJ2IjoiMSJ9.Uea0P6sEvDbGIaW6kkzobYKfoXMRrH7i1YnEArONCs0yTPBLA9NM5vOKCtQ9-UbdobpSp64xwHjo42hThSUoQ7fx3A72S4V6_bX8zNSeVEKRFII75lkSrDON-KAQSzNfMjAjpmSlV9YW-0CKucMBIsHo3E1osudS2ePiBgKMXJZP4Iki2zIsr6QKhE1SXmVEMOp7lgYtYye2gQOb_syhLkSQ0YaAW49pGxrMJX-oKqY.QoO_weVjlwylEr8JJ-JruCNNvDAa1rvOswism2x_-Eg%26dib_tag%3Dse%26keywords%3DSelfie%2BRing%2BLight%26qid%3D1748428953%26sprefix%3Dinstant%2Bcamera%252Caps%252C824%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1", "price":549},
        "flipkart": {"link": "https://www.flipkart.com/airtech-10-ring-light-camera-stand-7-ft-reels-video-stream-selfie-flash/p/itm65ad9edbb011c?pid=ACCGE72YWHN8UGCR&lid=LSTACCGE72YWHN8UGCRPIBQQI&marketplace=FLIPKART&q=InSelfie+Ring+Light&store=tyy%2F4mr%2Fkcr&srno=s_1_8&otracker=search&otracker1=search&fm=Search&iid=d611500b-047b-41fa-9ec5-64624d7d067c.ACCGE72YWHN8UGCR.SEARCH&ppt=sp&ppn=sp&ssid=jxio21kb4g0000001748428957628&qH=7117c3e984bd4d43", "price":550}
    },
    "Notebook Planner": {
        "image": "https://m.media-amazon.com/images/I/61GaQwZbzfL._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/sspa/click?ie=UTF8&spc=MTo4NTc1MDEwMzI3MTQ5NTUxOjE3NDg0MjkwNTQ6c3BfYXRmOjMwMDQyMjc2MTM0MjUzMjo6MDo6&url=%2FAmazon-Personal-Organizer-Setting-Productivity%2Fdp%2FB0DB1S6ZWY%2Fref%3Dsr_1_1_sspa%3Fcrid%3D20QOJ2CZ2K2ND%26dib%3DeyJ2IjoiMSJ9.TYri7LosO6LCv6Ues-oA_H1at6VqLbHfFpC_Lw9yj6ir7lMRb24MNDpi6jxCocFBVEAtTAtONy2hgMMrWwBrHOSecXcG1OLd7xSJQQ_2tpBjiTXX5N9njLjqBVambu-iaN3-_ujbxhMY5qNsvDH41ywEWx0jHY1vXOzuIcK0EwC5kuMh6YSqGbIlSdweFLfNfFj5VtBX0fT1JYcPW5zN1CiOTJMjXQaVYormXOi0xk6T_YXkOv8YPmrvOjx_66stwJhcBTRFeSWB3vaj7iZwcBfhLOgKfvWV1DEy42Js8GI.eLCsYoZrlnC-MxH8HtPwofdZaBI1xy5lJIRKgfgHC5Q%26dib_tag%3Dse%26keywords%3Dnotebook%2Bplanner%26qid%3D1748429054%26sprefix%3Dnotebook%2Bplanne%252Caps%252C330%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1", "price":229},
        "flipkart": {"link": "https://www.flipkart.com/mahavira-traders-005-a4-notebook-plain-500-pages/p/itm1338890aa0f7f?pid=DIAH2DFYEFF6G2TQ&lid=LSTDIAH2DFYEFF6G2TQV3CIFZ&marketplace=FLIPKART&q=Notebook+Planne&store=dgv&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=4a9bb766-1933-41f3-8a71-ac8daad379cc.DIAH2DFYEFF6G2TQ.SEARCH&ppt=sp&ppn=sp&ssid=iyg4qqbyn40000001748429058923&qH=5342d30c01535e34", "price":240}
    },
    "Perfume Gift Set": {
        "image": "https://m.media-amazon.com/images/I/61Z0HyOvTfL._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/Bella-Vita-Organic-Perfumes-Fragrance/dp/B09232XNTX/ref=sr_1_5?crid=WABZXLRLAYMS&dib=eyJ2IjoiMSJ9.K7sG3wbNLC41L-EuhEWj90tJOV7l36UY1Gh0B5H6iPomUAaIFzDdcK4tAeIUqBsG43bUM_1BPt7I9QV4a6DbdC4gaYC4FpejM4FEjJ8o_6XHjFIvFcxeAqhQNGxDw_cEw4YJPkBIQMfkJm9qop90aHzBJ5YjEWonJA99tWYZ56afs4N5Qw-qBvFMr3ndytpV-fq6WEUNbuAbviYB8YFN9gkrr1XhODH4MEKGXNF6AaK0VsKs9-PjQ20JIXjmq49xoBOm-B2jAdOh7rhWHuDUu0YC2MX8BPHAljIXRLe-HIw.nXb4Ev1Y1YeaU_UEWICa4rEgG-lUM0rMvP7tcEPG2yg&dib_tag=se&keywords=perfume+gift+set&qid=1748429254&sprefix=nperfume+gift+set%2Caps%2C312&sr=8-5", "price":552},
        "flipkart": {"link": "https://www.flipkart.com/bellavita-luxury-perfume-gift-set-long-lasting-fragrance-eau-de-parfum-80-ml/p/itmf17ee6c66d0f7?pid=PERG8TURAY7GWRRT&lid=LSTPERG8TURAY7GWRRTSKILX4&marketplace=FLIPKART&q=bellavita+rose&store=g9b%2F0yh&srno=s_1_27&otracker=search&otracker1=search&fm=Search&iid=ed222251-1e74-4722-b289-d27a085b9993.PERG8TURAY7GWRRT.SEARCH&ppt=sp&ppn=sp&ssid=zf9akhmu1c0000001748429359142&qH=6d3152e29baccee0", "price":540}
    },
    "Wallet": {
        "image": "https://m.media-amazon.com/images/I/71q7Fsywp9L._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/WILDHORN%C2%AE-Carter-Leather-Wallet-Oliver/dp/B08P5M592H/ref=sr_1_3?crid=38L93AENP9SZH&dib=eyJ2IjoiMSJ9.laje_yMNXp62Tidm3clmpuywXJg2teUMlOvx7EHwogO1-w6HuLwmdnfqF0F86xZGQsHwVkh7cyRuKxa9MTQk_2RHUpSJpDqLkT-Qkjt71JKjiFemUM21Td28wsQbe81W0XtkNXglz_VLu8KAJVaSkadGvcgrkjqi83VShW6r_6x7CLzrj8nV96BQoO9Wy2n9-PZAhiQnxwkLHbOWKKzBenQ674Q7s_QJM8xpEJKOuNN1pjyY6EBnmIcuzNNmOSiGxfi78BYkJVe7EA8-Hc4BIjeRpiZaKH-3R_xk2VZZQTU.1bT4L4c2Bs0euxi8JHXlIm60perLqp4TxdT7Y5ZTL0M&dib_tag=se&keywords=Wallet&qid=1748429423&sprefix=wallet%2Caps%2C264&sr=8-3", "price":480},
        "flipkart": {"link": "https://www.flipkart.com/wildhorn-men-casual-green-genuine-leather-wallet/p/itmcc1708af0aa5a?pid=WCWGM3HUK5DGRPVU&lid=LSTWCWGM3HUK5DGRPVUHADHSG&marketplace=FLIPKART&q=Wallet&store=reh%2Fcca%2Fh76&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=en_eo9MYxHNp3NVcw2VVtSjpVoLig8eHfw_dvkA7y4ogQ3suWPCZI5919oYCxVsnl3bwXfbQ3HhcwM5zz51Ugs_3A%3D%3D&ppt=sp&ppn=sp&ssid=zhmavw5o1s0000001748429418364&qH=156e132b014314b1", "price":455}
    },
    "Coffee Mug": {
        "image": "https://m.media-amazon.com/images/I/31zFYkIiwNL._AC_UL480_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/SR-Insulated-Restaurant-Milliliter-Multicolor/dp/B0CSX7NZ3K/ref=sr_1_16?crid=1SO47OKAY8JEL&dib=eyJ2IjoiMSJ9.DH043B34rjV0yBylyovIytJmRawjH_yJO6Uzqc2ZH-U_yTuJgGkhoaDr2vCaxBUhfAaeMYz1kRn6Ax8cR3NtzDojSSdIOYhDt2bMFn8bK2qhA3FpPryAnRVe8fX1e-a7FZZEkShuumArutYFhMuWq9r7H0_Se6-8mi-NYrL7rQ6Gjzg_sTFxrDCRyOqeQmJ8CMUb5zUFYYPGQ7x5IrO2uBojKRtkbiheBfgZFYmlT2mypqj_TOsAtqSbudoEPiF1uKLWSeSXWCDklJu6fn4K0SVypbsgXC8Fpc2NsDkKQww.R8GAvVmQOtNjPFwDrbi_lOikkTXLLrBRzkbnxZtBG2w&dib_tag=se&keywords=Coffee+Mug&qid=1748429500&sprefix=coffee+mug%2Caps%2C343&sr=8-16", "price":149},
        "flipkart": {"link": "https://www.flipkart.com/offyx-stainless-steel-tea-cup-coffee-lid-300-ml-grey-mug/p/itm2cfbac2bb86bd?pid=MUGGE2GCAWSQQHYS&lid=LSTMUGGE2GCAWSQQHYSFV5ZEP&marketplace=FLIPKART&q=Coffee+Mug&store=upp%2Fi7t%2Fmsi&srno=s_1_13&otracker=search&otracker1=search&fm=Search&iid=9c40cb27-48b0-4663-a6ea-05f262862e82.MUGGE2GCAWSQQHYS.SEARCH&ppt=sp&ppn=sp&ssid=yttuumbu800000001748429495428&qH=75f62e12b1de6619", "price":140}
    },
    "Office Organizer": {
        "image": "https://rukminim2.flixcart.com/image/612/612/xif0q/desk-organizer/e/q/s/file-holder-na-file-rack-holder-for-office-and-home-38-x-35-x-28-original-imagzybjcqwnyaku.jpeg?q=70",
        "amazon": {"link": "https://www.amazon.in/SOLDTRUE-Organiser-Letter-Documents-Organizer/dp/B0B2X2TQB6/ref=sr_1_13?crid=T9OCMC8KGL5M&dib=eyJ2IjoiMSJ9.ACxPZFQnVszkevwnfYW0GthsvfBlgkiqtOTiMu8iqtuePCCSnjQkJlK10Sz71-AIs--QqNcCV-MWscXmPjWmYNdJKn2Sp3kEQpCm2PvJndbtIGoAvkL-3Wv8xpZS3WwAh7mxNOMqH1gJOWvLhXdM2jZFZy4EuJQe1t4XxY77vPBJ7cvMy4GUHTgpmVKYFyao_3JvGAhmAbsBo4CBOWotdKFxUs_e0yH_w_pQskih9GT_FnG4T-o8lfBNEyZ9d_RJ-5S9aCxiq17gigM8dsdDsZbx-hCJ6MllAVohxzsFUK8.VaUIO2p-VW_zppkcE9BjccFIQtloK49yTOwi79Ga_QY&dib_tag=se&keywords=Office+Organizer&qid=1748429611&sprefix=office+organizer%2Caps%2C324&sr=8-13", "price":890},
        "flipkart": {"link": "https://www.flipkart.com/qatalitic-5-compartments-desk-organizer-letters-documents-files-papers-office-sorter-file-rack-holder-home-38-x-35-28-cm/p/itmbdea983d078bc?pid=DKOGZYBJSZFUDZRM&lid=LSTDKOGZYBJSZFUDZRM8TI5NR&marketplace=FLIPKART&q=Office+Organizer&store=dgv%2Ftkw%2Fhlr&srno=s_1_15&otracker=search&otracker1=search&fm=Search&iid=e3232800-d1c9-4dd7-ba2a-d17754564898.DKOGZYBJSZFUDZRM.SEARCH&ppt=sp&ppn=sp&ssid=61velscaj40000001748429600673&qH=6534b0e4a11594d9", "price": 1230}
    },
    "Power Bank": {
        "image": "https://m.media-amazon.com/images/I/61CRsa2N6aL._AC_UY327_FMwebp_QL65_.jpg",
        "amazon": {"link": "https://www.amazon.in/sspa/click?ie=UTF8&spc=MToxMTcxMjc2MDE5NjkxMzg5OjE3NDg0Mjk3Mzk6c3BfYXRmOjMwMDE1MzA5NTE5NjAzMjo6MDo6&url=%2FURBN-20000-22-5W-Charging-Output%2Fdp%2FB08JW1GVS7%2Fref%3Dsr_1_1_sspa%3Fcrid%3D39TJ0TIJ6SJT9%26dib%3DeyJ2IjoiMSJ9.swroFMxjuXDAYy4O6LIZOsjzfmdBbDDV4Iw7FReJUrINyUPRlHHD1gS3rOeGbg3o0XLssX2YEhjvOR0vw32sHuWIBneBPKq6xPmb3tLrtIpXii2uezvitLmzGS3YpUdR8-LDa93m2-UbVHd2eIvvG3-SyAMtfuBQoYVG4lsFjTnNCvDwhCOuvBHpLlbI-62n4GHHtBPCKDFBn9SauHtMyg3g9SPpvmFJqIC0lgaU1DA.cODntRttro_sKQQuLoe7X4jsA5NzZ2GRkKAXT5sdbYA%26dib_tag%3Dse%26keywords%3DPower%2BBank%26qid%3D1748429739%26sprefix%3Doffice%2Borganizer%252Caps%252C339%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1", "price":1229},
        "flipkart": {"link": "https://www.flipkart.com/urbn-10000-mah-22-5-w-ultra-compact-pocket-size-power-bank/p/itm56199a97e34ec?pid=PWBGWKCMMFVDEY6N&lid=LSTPWBGWKCMMFVDEY6NPBLV1X&marketplace=FLIPKART&q=Power+Bank&store=tyy%2F4mr%2Ffu6&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=en_yHuTlRjrNkpPWeNzlX4yQ3yAQiSAcVAfScfQUkwiZS3m7mE5atDKgHpgK4qKoZpxc4Jpl7O0j5EMpc6IxxbaFoQEIsITtCzc4bHaOMTqL08%3D&ppt=sp&ppn=sp&ssid=yk3xrvcbe80000001748429742602&qH=de84d710c8957c5e", "price":699}
    }
    # Add all other items here just like above...
}

# -----------------------------
# Gift Recommendation Function
# -----------------------------
def recommend_gifts(age, gender):
    age = int(age)
    if age <= 10 and gender == 'male':
        gift_names = ["Toy Car", "LEGO Set", "Superhero Costume", "RC Helicopter", "Puzzle Game"]
    elif age <= 10 and gender == 'female':
        gift_names = ["Doll Set", "Coloring Kit", "Story Book", "Princess Tent", "DIY Bracelet Kit"]
    elif 11 <= age <= 20 and gender == 'male':
        gift_names = ["Gaming Mouse", "Bluetooth Speaker", "Skateboard", "Football", "Wireless Earbuds"]
    elif 11 <= age <= 20 and gender == 'female':
        gift_names = ["Makeup Kit", "Instant Camera", "Selfie Ring Light", "Notebook Planner", "Perfume Gift Set"]
    else:
        gift_names = ["Watch", "Wallet", "Coffee Mug", "Office Organizer", "Power Bank"]

    recommended = []
    for name in gift_names:
        gift = gifts_data.get(name)
        if gift:
            cheaper_site = "amazon" if gift["amazon"]["price"] < gift["flipkart"]["price"] else "flipkart"
            gift_info = {
                "name": name,
                "image": gift["image"],
                "best_link": gift[cheaper_site]["link"],
                "best_price": gift[cheaper_site]["price"]
            }
            recommended.append(gift_info)
    return recommended

# -----------------------------
# Routes
# -----------------------------

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    phone = request.form['phone']
    password = request.form['password']
    if check_login(phone, password):
        return redirect(url_for('home'))
    else:
        return "<h3 style='color:red;text-align:center;'>Invalid login. <a href='/'>Try Again</a></h3>"

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    age = request.form['age']
    gender = request.form['gender']
    gifts = recommend_gifts(age, gender)
    return render_template('result.html', gifts=gifts)

# -----------------------------
# Run Server
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)

from bouquet_maker import BouquetMaker

def bouquet_maker():
    try:
        print("Starting bouquet maker...")
        bouquet_maker = BouquetMaker()
        bouquet_maker.run()

    except KeyboardInterrupt:
        print("Exiting bouquet maker...")


if __name__ == '__main__':
    bouquet_maker()

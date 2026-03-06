escolha = int(input("Escolha um dos computadores \n 1.Computador Gamer \n 2.Computador para Escritório \n 3.Computador para Estudo \n 4.Computador para Servidor\n "))

match escolha:
    case 1:
        print("Processador: AMD Ryzen 5 5500, Placa de Vídeo: NVIDIA RTX 3060, Memória RAM: 16GB, Armazenamento: SSD NVMe 500GB, Fonte: 650W, Placa-mãe: B550M")
    case 2:
        print("Processador (CPU): Intel Core i3-12100 / i5-12400, Memória RAM: 8GB DDR4, Armazenamento: SSD NVMe 512GB, Placa-mãe: H610 (Intel), Fonte: 400W a 500W")
    case 3:
        print("Processador (CPU): Intel Core i5-12400/13400, Memória RAM: 16GB, Armazenamento: SSD 512GB, Placa-mãe: B660/B760 (Intel), Fonte: 400W-500W")
    case 4:
        print("Processador: Intel Core i5-13400, Placa-mãe: Chipset B660/B760, Memória RAM: 16GB DDR4, Armazenamento: 2 x SSD 1TB NVMe PCIe 4.0, Fonte: 500W 80 Plus Bronze/Gold")
    
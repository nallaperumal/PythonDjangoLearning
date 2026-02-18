export class SnackItem {
    name: string;
    price: number;
    imageurl: string;

    constructor(name: string, price: number, imageurl: string) {
        this.name = name;
        this.price = price;
        this.imageurl = imageurl;
    }
}

export class SnackItem {
    id: number;
    name: string;
    price: number;
    imageurl: string;

    constructor(id: number, name: string, price: number, imageurl: string) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.imageurl = imageurl;
    }
}

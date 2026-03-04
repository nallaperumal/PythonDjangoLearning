export interface LoginToken {
    access: string;
    refresh: string;
}
export interface MovieItem {
    id: number;
    name: string;
    year_of_release: number;
    lang: string;
    imdb_rating: number;
    director: string;
}

export interface SongItem {
    id: number;
    name: string;
    running_time: number;
    singer: string;
}

export interface MovieWithSongItem {
    id: number;
    name: string;
    year_of_release: number;
    lang: string;
    imdb_rating: number;
    director: string;
    songs: SongItem[];

}
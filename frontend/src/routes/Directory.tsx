import React from "react";
import { useLoaderData, LoaderFunctionArgs } from "react-router-dom";
import axios from "axios";

import { api_url } from "../constants";

import styles from "../styles/Main.module.sass";

export interface ShortDirectoryItem {
    id: number,
    name: string,
}

export interface DirectoryItem extends ShortDirectoryItem{
    directory_name: string,
    description: string,
}

export const DirectoryNames = {
    MM: "Модель машины",
    EM: "Модель двигателя",
    TM: "Модель трансмиссии",
    DAM: "Модель ведущего моста",
    SAM: "Модель управляемого моста",
    MT: "Вид ТО",
    FN: "Узел отказа",
    RM: "Метод восстановления",
}

export async function loader({ params }: LoaderFunctionArgs): Promise<DirectoryItem> {
    const response = await axios.get<DirectoryItem>(`${api_url}directory/${params.id}/`);
    return response.data;
}

function Directory() {
    const data = useLoaderData() as DirectoryItem;
    return (<main className={styles.main}>
        <div><b>{ DirectoryNames[data.directory_name] }:</b> { data.name }</div>
        <div>{ data.description }</div>
    </main>)
}

export default Directory;
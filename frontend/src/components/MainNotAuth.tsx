import React, {useState} from "react";
import axios from "axios";
import Table from "./Table";
import { ShortDirectoryItem } from "../routes/Directory";

import {api_url} from "../constants";

import styles from "../styles/Main.module.sass";


export interface DataNotAuth {
    machine_number: string,
    engine_number: string,
    transmission_number: string,
    driving_axle_number: string,
    steering_axle_number: string,
    machine_model: ShortDirectoryItem,
    engine_model: ShortDirectoryItem,
    transmission_model: ShortDirectoryItem,
    driving_axle_model: ShortDirectoryItem,
    steering_axle_model: ShortDirectoryItem,
}

export const DATA_NOT_AUTH_KEYS = [
    "machine_model",
    "machine_number",
    "engine_model",
    "engine_number",
    "transmission_model",
    "transmission_number",
    "driving_axle_model",
    "driving_axle_number",
    "steering_axle_model",
    "steering_axle_number",
];

export const DATA_NOT_AUTH_COLUMNS = [
    "Модель машины",
    "Номер машины",
    "Модель двигателя",
    "Номер двигателя",
    "Модель трансмиссии",
    "Номер трансмиссии",
    "Модель ведущего моста",
    "Номер ведущего моста",
    "Модель управляемого моста",
    "Номер управляемого моста",
];

export const MACHINE_DIRECTORY_KEYS = new Set([
    "machine_model",
    "engine_model",
    "transmission_model",
    "driving_axle_model",
    "steering_axle_model",
]);

function MainNotAuth() {
    const [[data, numbers], setDataNumbers] = useState<[DataNotAuth[], Set<string>]>([[], new Set()]);

    async function find(e) {
        e.preventDefault();
        const response = await axios.get<DataNotAuth>(`${api_url}/machine/${e.target.number.value}/`);
        const responseData = response.data;
        if (numbers.has(responseData.machine_number)) { return; }
        data.push(responseData);
        numbers.add(responseData.machine_number);
        setDataNumbers([data, numbers]);
    }

    return (<main className={styles.main}>
        <form onSubmit={find}>
            <label>Заводской номер: <input type="text" name="number"/></label>
            <button type="submit">Поиск</button>
        </form>
        <div>Информация о комплекте и технические характеристиках Вашей техники</div>
        <Table
            columns={DATA_NOT_AUTH_COLUMNS}
            keys={DATA_NOT_AUTH_KEYS}
            directoryKeys={MACHINE_DIRECTORY_KEYS}
            uniqueKey="machine_number"
            data={data}
        />
    </main>);
}

export default MainNotAuth;
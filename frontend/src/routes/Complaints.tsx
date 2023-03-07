import React from "react";
import { redirect, useLoaderData, useOutletContext } from "react-router-dom";
import axios from "axios";

import Table from "../components/Table";
import Tabs from "../components/Tabs";
import { Auth } from "./Root";
import { ShortDirectoryItem } from "./Directory";

import styles from "../styles/Main.module.sass";
import { api_url } from "../constants";

export interface DataComplaints {
    id: number,
    machine: string,
    failure_date: Date,
    operating_time: number,
    failure_node: ShortDirectoryItem,
    failure_description: string,
    recovery_method: ShortDirectoryItem,
    spare_parts: string,
    recovery_date: Date,
    downtime: number,
    service_company: string,
}

export const DATA_COMPLAINTS_KEYS = [
    'machine',
    'failure_date',
    'operating_time',
    'failure_node',
    'failure_description',
    'recovery_method',
    'spare_parts',
    'recovery_date',
    'downtime',
    'service_company',
]

export const DATA_COMPLAINTS_COLUMNS = [
    'Машина',
    'Дата отказа',
    'Наработка, м/час',
    'Узел отказа',
    'Описание отказа',
    'Способ восстановления',
    'Используемые запасные части',
    'Дата восстановления',
    'Время простоя техники',
    'Сервисная компания',
]

export const COMPLAINTS_DIRECTORY_KEYS = new Set([
    'failure_node',
    'recovery_method',
]);

export async function loader(): Promise<DataComplaints[] | Response> {
    const token = localStorage.getItem("TOKEN");
    if (!token) return redirect("/");
    try {
        const response = await axios.get<DataComplaints[]>(api_url + 'complaint/', {
            headers: {
                Authorization: 'Token ' + token
            }
        });
        return response.data;
    } catch (error) {
        localStorage.removeItem("TOKEN");
        return redirect("/")
    }
}

function Complaints() {
    const { auth } = useOutletContext<{auth: Auth}>();
    const data = useLoaderData() as DataComplaints[];

    return (<main className={styles.main}>
        <div>{auth.user.name}</div>
        <div>Информация о Ваших рекламациях</div>
        <Table
            columns={DATA_COMPLAINTS_COLUMNS}
            keys={DATA_COMPLAINTS_KEYS}
            directoryKeys={COMPLAINTS_DIRECTORY_KEYS}
            uniqueKey="id"
            data={data}>
            <Tabs />
        </Table>
    </main>);
}

export default Complaints;
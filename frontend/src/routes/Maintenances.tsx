import React from "react";
import {redirect, useLoaderData, useOutletContext} from "react-router-dom";
import axios from "axios";

import Table from "../components/Table";
import Tabs from "../components/Tabs";
import {Auth} from "./Root";
import {ShortDirectoryItem} from "./Directory";

import styles from "../styles/Main.module.sass";
import {api_url} from "../constants";

export interface DataMaintenance {
    id: number,
    machine: string,
    maintenance_type: ShortDirectoryItem,
    date: Date,
    operating_time: number,
    work_order_number: string,
    work_order_date: Date,
    organization: string,
    service_company: string,
}

export const DATA_MAINTENANCE_KEYS = [
    'machine',
    'maintenance_type',
    'date',
    'operating_time',
    'work_order_number',
    'work_order_date',
    'organization',
    'service_company',
]

export const DATA_MAINTENANCE_COLUMNS = [
    'Машина',
    'Вид ТО',
    'Дата проведения ТО',
    'Наработка, м/час',
    '№ заказа-наряда',
    'Дата заказа-наряда',
    'Организация, проводившая ТО',
    'Сервисная компания',
];

export const MAINTENANCES_DIRECTORY_KEYS = new Set(['maintenance_type']);

export async function loader(): Promise<DataMaintenance[] | Response> {
    const token = localStorage.getItem("TOKEN");
    if (!token) return redirect("/");
    try {
        const response = await axios.get<DataMaintenance[]>(api_url + 'maintenance/', {
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

function Maintenances() {
    const { auth } = useOutletContext<{auth: Auth}>();
    const data = useLoaderData() as DataMaintenance[];

    return (<main className={styles.main}>
        <div>{auth.user.name}</div>
        <div>Информация о проведённых ТО Вашей техники</div>
        <Table
            columns={DATA_MAINTENANCE_COLUMNS}
            keys={DATA_MAINTENANCE_KEYS}
            directoryKeys={MAINTENANCES_DIRECTORY_KEYS}
            uniqueKey="id"
            data={data}>
            <Tabs />
        </Table>
    </main>);
}

export default Maintenances;
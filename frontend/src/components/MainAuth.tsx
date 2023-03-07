import React from "react";

import {DataNotAuth, DATA_NOT_AUTH_KEYS, DATA_NOT_AUTH_COLUMNS, MACHINE_DIRECTORY_KEYS} from "./MainNotAuth";
import Table from "./Table";
import Tabs from "./Tabs";

import styles from "../styles/Main.module.sass";


export interface DataAuth extends DataNotAuth {
    supply_contract: string,
    shipment_date: Date,
    consignee: string,
    delivery_address: string,
    complete_set: string,
    client: string,
    service_company: string,
}

export interface MainAuthProps {
    userName: string,
    data: DataAuth[],
}

export const DATA_AUTH_KEYS = DATA_NOT_AUTH_KEYS.concat([
    "supply_contract",
    "shipment_date",
    "consignee",
    "delivery_address",
    "complete_set",
    "client",
    "service_company",
])

export const DATA_AUTH_COLUMNS = DATA_NOT_AUTH_COLUMNS.concat([
    "Договор поставки №, дата",
    "Дата отгрузки с завода",
    "Грузополучатель",
    "Адрес поставки",
    "Комплектация ",
    "Клиент",
    "Сервисная компания",
])

export const DIRECTORY_KEYS = [];

function MainAuth({userName, data}: MainAuthProps) {
    return (<main className={styles.main}>
        <div>{userName}</div>
        <div>Информация о комплекте и технические характеристиках Вашей техники</div>
        <Table
            columns={DATA_AUTH_COLUMNS}
            keys={DATA_AUTH_KEYS}
            directoryKeys={MACHINE_DIRECTORY_KEYS}
            uniqueKey="machine_number"
            data={data}
        >
            <Tabs />
        </Table>
    </main>);
}

export default MainAuth;
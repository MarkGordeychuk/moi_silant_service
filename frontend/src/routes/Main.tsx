import React, {useState} from "react";
import {useOutletContext, useLoaderData} from "react-router-dom";
import axios from "axios";

import Table from "../components/Table";
import MainAuth, {DataAuth} from "../components/MainAuth";
import MainNotAuth, {DataNotAuth} from "../components/MainNotAuth";
import {Auth} from "./Root";

import {api_url} from "../constants";
import styles from "../styles/Main.module.sass";


export async function loader(): Promise<DataAuth[] | null> {
    const token = localStorage.getItem("TOKEN");
    if (!token) { return null; }
    const response = await axios.get<DataAuth[]>(api_url, {
        headers: {
            Authorization: 'Token ' + token
        }
    })
    console.log(response.data);
    return response.data;
}

export default function Main() {
    const { auth } = useOutletContext<{auth: Auth}>();
    return auth.auth ? (<MainAuth data={useLoaderData() as DataAuth[]} userName={auth.user.name}/>) : (<MainNotAuth />);
}
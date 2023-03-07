import React, {useState} from "react";
import {Outlet, useLoaderData} from "react-router-dom";
import axios from "axios";

import Header from "../components/Header";
import Footer from "../components/Footer";

import {api_url} from "../constants";

import styles from "../styles/Root.module.sass";

export interface Auth {
    auth: boolean,
    user?: any
}

export interface LoaderResponse {
    auth: Auth,
}

async function authLoader(): Promise<Auth> {
    const token = localStorage.getItem('TOKEN');
    if (!token) { return {auth: false}; }
    return (await axios.get<Auth>(api_url + "auth/", {
        headers: {
            Authorization: 'Token ' + token
        }
    })).data;
}


export async function loader(): Promise<LoaderResponse> {
    const [auth, ] = await Promise.all([
        authLoader()
    ]);
    return {
        auth: auth
    }
}

export default function Root() {
    const loaderData = useLoaderData() as LoaderResponse;
    const [auth, setAuth] = useState<Auth>(loaderData.auth);
    return (<div className={styles.root}>
        <Header />
        <Outlet context={{auth, setAuth}}/>
        <Footer />
    </div>);
}
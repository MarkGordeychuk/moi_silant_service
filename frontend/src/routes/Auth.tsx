import React, { Dispatch, SetStateAction } from "react";
import axios from "axios";
import { useNavigate, useOutletContext } from "react-router-dom";

import { Auth as RootAuth } from "./Root";

import { api_url } from "../constants";

export interface AuthResponse {
    auth: boolean,
    user?: any,
    token?: string,
}


export default function Auth() {
    const navigate = useNavigate();
    const {setAuth} = useOutletContext<{setAuth: Dispatch<SetStateAction<RootAuth>>}>();
    function submit(e) {
        e.preventDefault();
        axios.post<AuthResponse>(api_url + "auth/", {
            name: e.target.name.value,
            password: e.target.password.value
        }).then(response => {
            const data = response.data;
            console.log(response.data);
            if (data.auth) {
                localStorage.setItem("TOKEN", data.token);
                setAuth(data);
            }
            return navigate("/");
        }).catch(console.error);
    }

    return (<div>
        <form onSubmit={submit}>
            <label>
                Имя:
                <input type="text" name="name"/>
            </label>
            <label>
                Пароль:
                <input type="password" name="password"/>
            </label>
            <button type="submit">Авторизоваться</button>
        </form>
    </div>);
}
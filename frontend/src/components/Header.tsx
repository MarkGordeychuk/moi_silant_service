import React from "react";
import {Link} from "react-router-dom";

import Contacts from "./Contacts";

import styles from "/src/styles/Header.module.sass";
import img from "/src/files/logo.svg";

export default function Header() {
    return (<header className={styles.header}>
        <div className={styles.top}>
            <div className={styles.element}><Link to="/"><img src={img} height="40px"/></Link></div>
            <div className={styles.left}>
                <Contacts className={styles.element} />
                <div className={styles.element}><Link to="/auth/" className={styles.btn}>Авторизация</Link></div>
            </div>
        </div>
        <div className={styles.bottom}>
            Электронная сервисная книжка "Мой Силант"
        </div>
    </header>);
}
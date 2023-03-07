import React from "react";

import Contacts from "./Contacts";

import styles from "../styles/Footer.module.sass";


export default function Footer() {
    return (<footer className={styles.footer}>
        <Contacts />
    </footer>);
}
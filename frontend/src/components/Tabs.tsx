import React from "react";
import {Link} from "react-router-dom";

import styles from "../styles/Tabs.module.sass";

function Tabs() {
    return (<div className={styles.tabs}>
        <Link className={styles.btn} to='/'>Общая информация</Link>
        <Link className={styles.btn} to='/maintenances/'>ТО</Link>
        <Link className={styles.btn} to='/complaints/'>Рекламации</Link>
    </div>)
}

export default Tabs;